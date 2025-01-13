# Aerith AI

Aerith AI is an advanced AI-driven platform that create personal virtual girlfriend for individual who tired of facing real girlfriend and Aerith will fulfil all your fantasy needs.

## Features

- **Dynamic X Integration**: Automatically monitors and processes user tweets in real-time to generate responses and deliver PFPs.
- **Sophisticated Image Generation Pipeline**: Utilizes multi-layered AI models combining generative adversarial networks (GANs) and diffusion techniques to produce high-quality, manga-style artwork.
- **Adaptive Styling**: AI analyzes user input and X metadata (e.g., profile bio, activity) to tailor PFP designs uniquely for each individual.
- **Scalable Architecture**: Built with modular components for performance and scalability, ensuring fast response times even under heavy user interaction.

## Installation

### Prerequisites
- Python 3.9 or higher
- X API credentials for integration
- Docker (for optional containerized deployment)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/OtakuAI.git
   cd Aerith AI
   pip install -r requirements.txt
   ```
2. Set up your `.env` file with the following keys:
   ```
   X_API_KEY=your_api_key
   X_API_SECRET=your_api_secret
   X_ACCESS_TOKEN=your_access_token
   X_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```
3. (Optional) Set up Redis for task queuing:
   ```bash
   docker run -d --name Aerith AI-redis -p 6379:6379 redis
   ```
4. Run the bot:
   ```bash
   python main.py
   ```

## Key Functionalities

Aerith AI doesn't just create images—it understands the user. By analyzing tweet content and user metadata, it tailors the PFP to match the user’s mood, interests, and personality. 
## Contribution

We welcome contributions! If you’d like to enhance Aerith AI or add new features, feel free to submit a pull request. Be sure to follow the repository's coding guidelines.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For inquiries, support, or suggestions, contact us at https://https://x.com/AerithAiGf.
