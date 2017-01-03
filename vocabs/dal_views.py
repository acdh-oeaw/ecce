from dal import autocomplete
from .models import SkosLabel, SkosConcept, SkosConceptScheme


class SKOSConstraintAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        scheme = self.request.GET.get('scheme')
        try:
            selected_scheme = SkosConceptScheme.objects.get(dc_title=scheme)
            qs = SkosConcept.objects.filter(scheme=selected_scheme)
        except:
            qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class SkosLabelAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosLabel.objects.all()

        if self.q:
            qs = qs.filter(label__icontains=self.q)

        return qs


class SkosConceptAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosConcept.objects.all()

        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)

        return qs


class SkosConceptSchemeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SkosConceptScheme.objects.all()

        if self.q:
            qs = qs.filter(dc_title__icontains=self.q)

        return qs
