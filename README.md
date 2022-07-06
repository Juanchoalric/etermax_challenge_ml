# etermax_challenge_ml

### Google Colab link to get the notebook where the model is created

https://colab.research.google.com/drive/1o4_TnM62iJCTwikvrZcfMOxkSdv2ps5k?usp=sharing

### Running the application

1. Install python 3.8 or higher.
2. Run 'pip install -r requirements.txt' to install all the necesary dependencies.
3. Run "python app.py" to start the application
4. Use your favorite tool for doing http request (for example: Postman or just the requests python package)
5. http://127.0.0.1:5000/predict us this url
6. Pass this json structure as the body of the response

{
    "country": "es",
    "source": "Organic",
    "platform": "Android",
    "device_family": "Apple iPhone",
    "event_1": 101,
    "event_2": 8
}

7. You will recieve a json with the response

{
    "prediction": 0.2694689929485321
}

8. You could also run 'docker build -t etermax . && docker run --rm -it -p 5000:5000 etermax' if you got Docker install.
