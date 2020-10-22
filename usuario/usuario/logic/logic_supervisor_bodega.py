from ..models import SupervisorBodega, BodegaSupervisor


def create_supervisor(form):
    """
    Creacion de un supervisor de bodega
    :param form:
    :return:
    """
    supervisor = form.save()
    supervisor.save()
    return ()


def get_all_supervisores():
    """
    Todos los supervisores de bodega de chiper
    :return: QuerySet con los supervisores
    """
    supervisores = SupervisorBodega.objects.all()
    return supervisores


def get_all_bodegas_supervisor():
    """
    Todas las bodegas asociadas a un supervisor
    :return: QuerySet de todas las bodegas con supervisor
    """
    bodegas_supervisores = BodegaSupervisor.objects.all()
    return bodegas_supervisores


def get_supervisor(i):
    """
    Supervisor de bodega con id especifico
    :param i: id buscado
    :return: supervisor con id especifico
    """
    supervisor = SupervisorBodega.objects.get(id=i)
    return supervisor


def get_supervisor_bodega(i):
    """
    Bodega asociada al supervisor con id especifico
    :param i: id del supervisor
    :return: bodega asociada al supervisor
    """
    bodega_supervisor = BodegaSupervisor.objects.get(supervisor=i)
    return bodega_supervisor


def create_bodega_supervisor(bodega, supervisor):
    """
    Crea asociacion entre bodega y supervisor
    :param bodega: id de bodega
    :param supervisor: supervisor
    :return:
    """
    if len(BodegaSupervisor.objects.filter(supervisor=supervisor)) > 0:
        raise Exception('Ya el supervisor se encuentra asociado')

    bodega_supervisor = BodegaSupervisor()
    bodega_supervisor.supervisor = supervisor
    bodega_supervisor.bodega = bodega
    bodega_supervisor.save()
    return ()
