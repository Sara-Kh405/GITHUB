import numpy as np
import librosa
import soundfile as sf
import pickle
from sklearn.preprocessing import MinMaxScaler


class ADALINEDenoiser:
    def __init__(self, weights = None, bias = None, window_size = 5):
        self.weights = weights
        self.bias = bias
        self.window_size = window_size

    def save_model(self, full_path):
        try:
            with open(full_path, 'wb') as f:
                pickle.dump({     
                    'weights':self.weights,
                    'bias':self.bias,
                    'window_size':self.window_size
                }, f)
        except Exception as e:
            print(f"Error is: {e}")

    @classmethod
    def load_model(cls, full_path):
        #Load a pre_trained
        try:
            with open(full_path, 'rb') as f:
                data = pickle.load(f)
            return cls(weights = data['weights'],
                    bias = data['bias'],
                    window_size = data['window_size'])
        except Exception as e:
            print(f"The error is {e}!!")

    def activation(self, x):
        #Linear activation function
        return x
    def predict(self, x):
        #Make a prediction with the pre_train weights
        return self.activation(np.dot(x, self.weights) + self.bias)

    def denoise_frame(self, noisy_frame):
        #Dinoise a single audio frame
        #Ensure the input frame matchs expected window size
        if len(noisy_frame) != self.window_size:
            raise ValueError(f"input frame size {len(noisy_frame)} must match window size {self.window_size}")

        return self.predict(noisy_frame)

    def denoise_audio(self, noisy_audio_file, cleaned_audio_file):
        #Denoise an entire audio file
        #Losd and preprocses audio
        y, sr = librosa.load(noisy_audio_file, sr = None)
        scaler = MinMaxScaler(feature_range=(-1, 1))
        y = scaler.fit_transform(y.reshape(-1, 1)).flatten()

        #pad the audio for processing
        pad_size = self.window_size // 2
        padded_noisy = np.pad(y, (pad_size, pad_size), mode = 'reflect') 

        #Process each sample
        denoised = np.zeros_like(y)
        for i in range(len(y)):
            window = padded_noisy[i:i+self.window_size]
            denoised[i] = self.denoise_frame(window)

        #Save denoised audio
        sf.write(cleaned_audio_file, denoised, sr)
        return denoised, sr

#Example usage(After Training)
if __name__ == "__main__":
    full_path = "mymodel.pkl"
    model = ADALINEDenoiser()
    model.save_model(full_path)
    denoiser = ADALINEDenoiser.load_model(full_path)
    input_audio = "noisy_audio.wav"
    output_audio = "cleaned_audio.wav"
    print(f"Denoising {input_audio} ...")
    denoised, sr = denoiser.denoise_audio(input_audio, output_audio)
    print(f"Denoised audio saved to {output_audio}")