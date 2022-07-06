import pandas as pd

class Prediction():

    @classmethod
    def predict(cls, data: dict, learner) -> dict:
        
        df = pd.DataFrame([[data["country"], 
                       data["source"], 
                       data["platform"], 
                       data["device_family"], 
                       data["event_1"], 
                       data["event_2"]
                    ]],
        columns=["country", 
                 "source", 
                 "platform", 
                 "device_family", 
                 "event_1", 
                 "event_2"
            ]
        )

        dl = learner.dls.test_dl(df, bs=256)
        preds, _ = learner.get_preds(dl=dl)

        return {"prediction": float(preds[0][0])}


