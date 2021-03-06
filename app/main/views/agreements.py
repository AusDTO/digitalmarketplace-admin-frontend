from flask import current_app, render_template
from flask_login import login_required
from dateutil.parser import parse as parse_date

from dmutils.formats import DateFormatter
from dmutils.documents import SIGNED_AGREEMENT_PREFIX

from .. import main
from ..auth import role_required
from ... import data_api_client


@main.route('/agreements/<framework_slug>', methods=['GET'])
@login_required
@role_required('admin', 'admin-ccs-sourcing')
def list_agreements(framework_slug):
    framework = data_api_client.get_framework(framework_slug)['frameworks']
    supplier_frameworks = data_api_client.find_framework_suppliers(
        framework_slug, agreement_returned=True
    )['supplierFrameworks']

    date_formatter = DateFormatter(current_app.config['DM_TIMEZONE'])
    for supplier_framework in supplier_frameworks:
        supplier_framework['agreementReturnedAt'] = date_formatter.datetimeformat(
            parse_date(supplier_framework['agreementReturnedAt']))

    return render_template(
        'view_agreements.html',
        framework=framework,
        supplier_frameworks=supplier_frameworks,
        signed_agreement_prefix=SIGNED_AGREEMENT_PREFIX
    )
