def process(request):
    data = request.form.to_dict()
    sender = str(data['Sender'])
    receiver = str(data['To'])
    subject = str(data['Subject'])
    message = str(data['body-html'])
    response = 'From: {}\nTo: {}\nSubject: {}\nMessage: {}'.format(sender, receiver, subject, message)
    return response
