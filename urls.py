# coding: utf-8

from django.conf.urls import url
from django.views import static

import views
import images

urlpatterns = [
    url(r'^$', views.index),
    url(r'^time/?$', views.current_time),
    url(r'^imageNew/?$', views.imageNew),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),
    url(r'^image/text?$', images.image_text),
    url(r'^image/filters/contour?$', images.filter_contour),
    url(r'^image/filters/detail?$', images.filter_detail),
    url(r'^image/filters/edge_enhance?$', images.filter_edge_enhance),
    url(r'^image/filters/edge_enhance_more?$', images.filter_edge_enhance_more),
    url(r'^image/filters/emboss?$', images.filter_emboss),
    url(r'^image/filters/find_edges?$', images.filter_find_edges),
    url(r'^image/filters/smooth?$', images.filter_smooth),
    url(r'^image/filters/smooth_more?$', images.filter_smooth_more),
    url(r'^image/filters/sharpen?$', images.filter_sharpen),
    url(r'^image/filters/gaussian_blur?$', images.filter_gaussian_blur),
    url(r'^image/filters/unsharp_mask?$', images.filter_unsharp_mask)

]
