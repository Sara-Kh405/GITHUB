import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler  #نرمال سازی

class ADALINE:
    def __init__(self, input_size, learning_rate=0.001, epochs=500):
        self.weights = np.random.randn(input_size) #****
        self.bias = np.random.randn()
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.loss_history = []

    def activation(self, x):
        """Linear activation function for ADALINE"""
        return x

    def predict(self, x):
        """Make a prediction"""
        return self.activation(np.dot(x, self.weights) + self.bias)
    
    def train(self, X, y):
        """Train the ADALINE network"""
        for _ in range(self.epochs):
            total_loss = 0
            for xi, target in zip(X, y):
                # Calculate prediction
                prediction = self.predict(xi)
                
                # Calculate error (difference between prediction and target)
                error = target - prediction
                total_loss += error**2
                
                # Update weights and bias
                self.weights += self.learning_rate * error * xi #****
                self.bias += self.learning_rate * error
            
            # Store mean squared error for this epoch
            self.loss_history.append(total_loss / len(y))
        
        return self.loss_history
    
    def denoise_frame(self, noisy_frame, context_size): #این تابع یک پنجره را تمیز میکند
        """Denoise a single frame using the trained ADALINE"""
        # Create input vector with context
        input_vec = np.zeros(len(self.weights))
        center = len(self.weights) // 2
        start = max(0, center - context_size)
        end = min(len(input_vec), center + context_size + 1)
        input_vec[start:end] = noisy_frame
        
        # Predict clean sample
        return self.predict(input_vec)

def preprocess_audio(file_path, sr=50000):
    """Load and preprocess audio file"""
    # Load audio file
    y, sr = librosa.load(file_path, sr=sr)
    
    # Normalize audio between -1 and 1
    scaler = MinMaxScaler(feature_range=(-1, 1))
    y = scaler.fit_transform(y.reshape(-1, 1)).flatten()
    
    return y, sr

def create_training_data(clean_audio, noisy_audio, window_size):
    """Create training data from clean and noisy audio pairs"""
    X = []
    y = []
    
    # Pad the audio signals to allow centered windows
    pad_size = window_size // 2
    padded_noisy = np.pad(noisy_audio, (pad_size, pad_size), mode='reflect')
    
    for i in range(len(clean_audio)):
        # Get window around current sample from noisy audio
        window = padded_noisy[i:i+window_size]
        X.append(window)
        
        # Corresponding clean sample is the target
        y.append(clean_audio[i])
    
    return np.array(X), np.array(y)

def train_adaline_for_denoising(clean_file, noisy_file, window_size=100, learning_rate=0.0001, epochs=500):
    """Train ADALINE for audio denoising"""
    # Load and preprocess audio files
    clean_audio, sr = preprocess_audio(clean_file)
    noisy_audio, _ = preprocess_audio(noisy_file, sr=sr)
    
    # Create training data
    X, y = create_training_data(clean_audio, noisy_audio, window_size)
    
    # Initialize and train ADALINE
    adaline = ADALINE(input_size=window_size, learning_rate=learning_rate, epochs=epochs)
    loss_history = adaline.train(X, y)
    
    # Plot training loss
    plt.plot(loss_history)
    plt.title('Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Mean Squared Error')
    plt.show()
    
    return adaline, sr

def denoise_audio(noisy_file, adaline, output_file, context_size=50):
    """Denoise an audio file using trained ADALINE"""
    # Load and preprocess noisy audio
    noisy_audio, sr = preprocess_audio(noisy_file)

    # Pad the audio for processing
    window_size = len(adaline.weights)
    pad_size = window_size // 2
    padded_noisy = np.pad(noisy_audio, (pad_size, pad_size), mode='reflect')
    
    # Denoise each sample
    denoised = np.zeros_like(noisy_audio)
    for i in range(len(noisy_audio)):
        window = padded_noisy[i:i+window_size]
        denoised[i] = adaline.denoise_frame(window, context_size)
    
    # Save denoised audio
    sf.write(output_file, denoised, sr)
    return denoised, sr

# Example usage
if __name__ == "__main__":
    # You need to have clean and noisy versions of the audio for training
    clean_audio_file = "original_audio.wav"
    noisy_audio_file = "noisy_audio.wav"
    audio_to_denoise = "noisy_audio.wav"
    output_file = "denoised_audio5.wav"
    
    # Train the ADALINE
    print("Training ADALINE for denoising...")
    adaline, sr = train_adaline_for_denoising(
        clean_audio_file, 
        noisy_audio_file,
        window_size=100,       # Size of the input window (odd number recommended)
        learning_rate=0.0001, # Learning rate
        epochs=500           # Number of training epochs
    )
    
    # Denoise new audio
    print("Denoising audio...")
    denoised_audio, sr = denoise_audio(audio_to_denoise, adaline, output_file)
    
    print(f"Denoised audio saved to {output_file}")