from flask import Blueprint


main = Blueprint('main', __name__)

from .views import (  # noqa
    login,
    agencies,
    agreements,
    communications,
    service_updates,
    services,
    suppliers,
    stats,
    users,
    buyers,
    applications,
    assessments,
    evidence_assessments,
    evidence,
    zendesk)
from app.main import errors  # noqa
