from typing import Any, ClassVar

from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView


class SessionExampleView(TemplateView):
    template_name = "session_experiments/index.html"

    KEY: ClassVar[str] = "count_of_visits"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        count_of_visits = request.session.get(self.KEY, 0)
        request.session[self.KEY] = count_of_visits + 1

        context = self.get_context_data(
            **{
                "session": request.session.session_key,
                "count_of_visits": count_of_visits,
            }
        )
        return self.render_to_response(context)
