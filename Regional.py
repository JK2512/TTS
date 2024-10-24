from TTS.utils.manage import ModelManager
from TTS.config.shared_configs import BaseTTSConfig
from TTS.trainer import Trainer

# Path to your dataset (must be formatted as required by Coqui TTS)
dataset_path = "/path/to/your/hindi/dataset"

# Load the pre-trained TTS model
model_name = "tts_models/en/ljspeech/tacotron2-DDC"  # Replace with Hindi or other regional TTS models if available
model_manager = ModelManager()
model_path = model_manager.download_model(model_name)

# Configuration for fine-tuning
config = BaseTTSConfig()
config.output_path = "output_finetuned"  # Where to save the fine-tuned model
config.model_path = model_path           # Path to pre-trained model
config.dataset = dataset_path            # Path to your regional language dataset
config.batch_size = 16                   # Adjust according to your system resources
config.num_epochs = 10                   # Number of training epochs

# Initialize the Trainer with the above configuration
trainer = Trainer(config)

# Start fine-tuning
trainer.fit()

print("Fine-tuning complete. Model saved to", config.output_path)
