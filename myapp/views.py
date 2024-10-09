from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@csrf_exempt
def process_input(request):
    if request.method == 'POST':
        input_string = request.POST.get('inputString')

        # Get the channel layer
        channel_layer = get_channel_layer()
        
        # Send the input string to the WebSocket group
        async_to_sync(channel_layer.group_send)(
            "results_group",
            {
                "type": "send_input",
                "input_string": input_string,
            }
        )

        # Redirect to the output page
        return redirect('output', input_id=input_string)

def output_page(request, input_id):
    return render(request, 'myapp/output.html', {'input_id': input_id})
