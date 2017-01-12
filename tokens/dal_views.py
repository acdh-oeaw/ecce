from dal import autocomplete
from .models import Cluster, Token

class ClusterAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Cluster.objects.all()
        if self.q:
            qs = qs.filter(consonant__startswith=self.q)
            
        return qs


class TokenModelAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Token.objects.all()
        if self.q:
            qs = qs.filter(plain_word__icontains=self.q)
            
        return qs


class TokenAC(autocomplete.Select2ListView):

    def get_list(self):
        plain_words = Token.objects.filter(plain_word__icontains=self.q)
        region_names_labels = set([x.plain_word for x in plain_words])
        return region_names_labels