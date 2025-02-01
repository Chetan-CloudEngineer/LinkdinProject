# instal an external module and use it to perform and operation of interest
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the poem
poem = """
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark;
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
"""

# Set the properties of the engine
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Convert text to speech
engine.say(poem)

# Wait for the speech to finish
engine.runAndWait()
