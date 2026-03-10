# Transformer Day 1 Exercise - Saud Ahmed

## 1. What is Generative AI?

Generative AI refers to artificial intelligence systems that can create new content such as text, images, audio, or code based on patterns learned from data. Instead of only analyzing or classifying information, generative models produce entirely new outputs that resemble the training data.

Traditional machine learning models usually perform tasks like classification or prediction. For example, a model may classify emails as spam or not spam. Generative AI, on the other hand, generates new data such as writing an article, creating artwork, or generating realistic images.

Generative AI is powered by deep learning models such as transformers and diffusion models. These models learn complex patterns in large datasets and use that knowledge to generate new outputs.

Real world applications include:
- AI chat assistants
- AI image generation
- Code generation systems

These systems are transforming industries by automating creative and analytical tasks.


## 2. Self Attention Explained

Example sentence:

"The cat sat on the mat"

Self-attention allows each word in a sentence to look at other words and determine how important they are for understanding context.

Query (Q) represents the word asking for context.

Key (K) represents the identity of each word.

Value (V) represents the information stored in each word.

The attention mechanism calculates similarity between queries and keys to determine which words should influence each other.

Scaling by √d_k prevents extremely large values in the dot product which could make softmax unstable.

Softmax converts attention scores into probabilities so that they sum to 1.

Attention solves the long-distance dependency problem that RNNs struggled with by allowing each token to directly attend to any other token in the sequence.


## 3. Encoder vs Decoder

| Component | Encoder | Decoder |
|-----------|--------|--------|
| Self Attention | Yes | Yes |
| Masked Attention | No | Yes |
| Cross Attention | No | Yes |
| Purpose | Understand input | Generate output |

Masked attention prevents the decoder from seeing future tokens during generation.

Cross attention allows the decoder to focus on encoder outputs when generating text.


## 4. Vision Transformers (ViT)

Vision Transformers apply the transformer architecture to images instead of text.

Images are first divided into small patches, for example 16x16 pixels. Each patch is flattened and converted into a vector. These vectors act like tokens in a text sequence.

The patch embeddings are then passed into a transformer encoder just like word tokens in natural language processing.

Positional embeddings are added so the model understands the spatial location of each patch in the image.

Unlike convolutional neural networks (CNNs) which process images using local filters, Vision Transformers rely entirely on self-attention to capture relationships between different regions of the image.

This allows the model to capture long-range dependencies across the entire image and can lead to strong performance when trained on large datasets.