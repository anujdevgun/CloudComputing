def lambda_handler(event, context):

    message = ''
    if event['message'] == 'Hi':
        message = "Hello"
    if event['message'] == 'hi':
        message = "Hello"
    if event['message'] == 'Hello':
        message = "Hello"
    if event['message'] == 'hello':
        message = "Hello"
    if event['message'] == 'Who made you':
        message = "ad4315 for assignment 1"
    if event['message'] == 'How are you':
        message = "Good"
    return message
