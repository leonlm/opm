# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import mixins, viewsets


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass


class ModelViewSetLRC(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """
    list(), retrieve(), create()
    """
    pass


class ModelViewSetLC(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """
    list(), create()
    """
    pass


class ModelViewSetU(mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    update()
    """
    pass


class ModelViewSetL(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    list()
    """
    pass

class ModelViewSetC(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    create()
    """
    pass


class ViewSet(viewsets.ViewSet):
    pass

