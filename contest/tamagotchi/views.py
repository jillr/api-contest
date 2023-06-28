from django.contrib.auth.models import User
from rest_framework import generics, mixins, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from tamagotchi.permissions import IsOwnerOrReadOnly
from tamagotchi.models import Pet
from tamagotchi.serializers import PetSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404
from datetime import datetime, timezone
from django.http import HttpResponseRedirect


class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


def feed(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.fed = datetime.now(timezone.utc)
    pet.save(update_fields=['fed'])
    return HttpResponseRedirect(reverse("tamagotchi:pet-detail", args=(pet.id,)))


def play(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.interacted = datetime.now(timezone.utc)
    pet.save(update_fields=['interacted'])
    return HttpResponseRedirect(reverse("tamagotchi:pet-detail", args=(pet.id,)))


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "pets": reverse("pet-list", request=request, format=format),
        }
    )