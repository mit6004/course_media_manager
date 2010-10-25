import django_filters
from tutorials.models import *

class TopicAssignmentFilterSet(django_filters.FilterSet):

    num_student_favorites=django_filters.NumberFilter(lookup_type='gt')
    num_staff_favorites=django_filters.NumberFilter(lookup_type='gt')

    class Meta:
        model=TopicAssignment
        list_filter=['topic']
        fields=['topic', 'video__author', 'video__type', 'video__semester', 'num_student_favorites']

    

    def __init__(self, *args, **kwargs):
        super(TopicAssignmentFilterSet, self).__init__(*args, **kwargs)
#        self.filters['topic'].extra.update( {'empty_label':u'--All Topics--'} )
#        self.filters['video__author'].extra.update( {'empty_label':u'--All Topics--'} )
#        self.filters['video__type'].extra.update( {'empty_label':u'--All Authors--'} )
#        self.filters['video__semester'].extra.update( {'':u'--All Terms--'} )

