import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

logger = logging.getLogger(__name__)


@csrf_exempt
def verification(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get('code', '')

            logger.info(f'Received code: {code}')

            # if the code is 6 digits and last digit is not 7
            if len(code) != 6 or not code.isdigit() or code[-1] == '7':
                logger.info(f'Validation failed for code: {code}')  # Log validation failure
                return JsonResponse({'status': 'error', 'message': 'Verification Error'}, status=400)

            # validation
            return JsonResponse({'status': 'success'}, status=200)

        except json.JSONDecodeError:
            logger.error('Invalid JSON data received')
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)

        except KeyError:
            logger.error('Missing required fields')
            return JsonResponse({'status': 'error', 'message': 'Missing required fields'}, status=400)

        except Exception as e:
            logger.error(f'An error occurred: {str(e)}')
            return JsonResponse({'status': 'error', 'message': f'An error occurred: {str(e)}'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
