from dal import autocomplete
from .models import Cluster

class ClusterAC(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Cluster.objects.all()
        if self.q:
            qs = qs.filter(consonant__startswith=self.q)
            
        return qs