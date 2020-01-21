from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("celebs-id")
model_trainer.trainModel(num_objects=10, num_experiments=50, enhance_data=True, batch_size=32, show_network_summary=True)
