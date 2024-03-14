from django.shortcuts import render, get_object_or_404
from django.http import Http404
from Client_User.models import Report,File,Appointment,Client,Vet,Log_in, Pets,rating
from django.shortcuts import render, redirect

def homeClient(request, id_cliente):

    client = Client.objects.get(pk=id_cliente)
    pets = Pets.objects.filter(client_id=client)

    return render(request, 'homeClient.html', {'pets': pets, 'client': client})

def registerPet(request):
    return render(request, 'registerPet.html')

def rateVet(request, id_client, vet_id):
    client=Client.objects.get(pk=id_client)
    vet_id= Vet.objects.get(pk=vet_id)
    appointment= rating.objects.filter(client_id=client).filter(vet_id=vet_id)
    if appointment and request.GET.get('rating')!=None:
        appointment.update(comment=request.GET.get('comment'))
        appointment.update(rating=request.GET.get('rating'))
        appointment=appointment[0]
    elif vet_id!=None and client!=None and request.GET.get('rating')!=None:
        ratings= rating.objects.all().order_by('-rating_id').first()
        if(ratings==None):
            appointment= rating(0,vet_id.vet_id,client.client_id,request.GET.get('comment'), request.GET.get('rating'))
            appointment.save()
        else:
            appointment= rating(ratings.rating_id+1,vet_id.vet_id,client.client_id,request.GET.get('comment'), request.GET.get('rating'))
            appointment.save()
    else:
        appointment=appointment.get(vet_id=vet_id)
    print(client.client_id)
    print(client)
    return render(request, 'rateVet.html',{'appointment':appointment,'client':client,'rate':appointment.rating,'com':appointment.comment})
def vaccineScore(schema, vaccines):
    score=0
    for i in vaccines:
        if(i.vaccine.vaccine_name in schema):
            score+=i.vaccine.score_value
    return score
def dataAnalysis(RACE_BREED_ICM):
    #ICM is equal to Weight(kg)/((Hight)^2)
    pass
def datAnalysis2(Race_Breed_Weight,Hight):
    
    pass