from ..models import Tendero


def get_all_tenderos():
    tenderos = Tendero.objects.all()
    return tenderos


def create_a_tendero(form):
    tendero = form.save()
    tendero.save()
    return ()
