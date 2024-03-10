# error_reporting/middleware.py

import logging
import traceback
from django.db import IntegrityError
from .models import ErrorReport

class ErrorReportingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        error_message = str(exception)
        traceback_info = traceback.format_exc()
        print("Error message: ", error_message)
        print("Traceback info: ", traceback_info)
        try:
            existing_report = ErrorReport.objects.filter(
                error_message=error_message,
                traceback=traceback_info
            ).exists()

            if not existing_report:
                ErrorReport.objects.create(
                    error_message=error_message,
                    traceback=traceback_info
                )
            else:
                self.logger.warning("Duplicate error report detected: %s", error_message)
        except IntegrityError:
            self.logger.error("Error occurred while saving error report to the database.")
