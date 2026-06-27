import soundfile as sf
import numpy as np

def add_noise_to_audio(input_file, output_file, noise_level=0.01):
    """
        Adds random noise to an audio file.

    Args:
        input_file (str): Path to the original audio file.
        output_file (str): Path to save the noisy audio file.
        noise_level (float): Controls the intensity of the noise.
                             Higher values mean more noise.
    """
    # Load the original audio
    try:
        audio_data, sr = sf.read(input_file)
    except Exception as e:
        print(f"Error reading audio file {input_file}: {e}")
        return
    # Generate random noise with the same shape as the audio data
    # Using 'normal' distribution for noise (Gaussian noise)
    noise = np.random.normal(0, noise_level, audio_data.shape)

    # Add noise to the audio data
    noisy_audio_data = audio_data + noise

    noisy_audio_data = np.clip(noisy_audio_data, -1.0, 1.0)

    # Save the noisy audio to a new file
    try:
        sf.write(output_file, noisy_audio_data, sr)
        print(f"Noisy audio saved to {output_file}")
    except Exception as e:
        print(f"Error writing audio file {output_file}: {e}")


original_audio_path = "original_audio.wav" # Make sure this file exists
noisy_audio_path = "noisy_audio.wav" # This will be the input for your denoiser

# Add noise to the audio file
# You can adjust the noise_level. Start with a small value like 0.01 or 0.05.
add_noise_to_audio(original_audio_path, noisy_audio_path, noise_level=0.05)
