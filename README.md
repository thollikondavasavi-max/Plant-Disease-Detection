# Plant AI - Disease Detection with Groq AI

A Flask web application that uses Groq AI to provide intelligent plant care advice and general plant health guidance through an AI-powered chat assistant.

## Features

- **AI-Powered Chat Assistant**: Get expert plant care advice, disease diagnosis help, and treatment recommendations
- **Image Upload Interface**: Upload plant images and receive general plant health guidance
- **Intelligent Conversations**: Ask detailed questions about plant symptoms, care, diseases, and treatments
- **Real-time Analysis**: Get instant responses with practical advice and recommendations
- **Responsive Design**: Works on desktop and mobile devices

## Important Note

**Vision Analysis Update**: Groq's vision models have been decommissioned. The app now focuses on providing expert plant care advice through the intelligent chat assistant. For accurate plant diagnosis, users can describe their plant's symptoms in detail to the AI assistant.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the API key

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

### 4. Run the Application

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Usage

### Plant Care Chat Assistant
1. Click the floating AI assistant button (🤖) on any page
2. Describe your plant's symptoms in detail:
   - "My tomato plant has yellow leaves with brown spots"
   - "What's causing white powder on my rose leaves?"
   - "My plant is wilting despite regular watering"
3. Get expert diagnosis and treatment recommendations
4. Ask follow-up questions for clarification

### Image Upload (General Guidance)
1. Go to the main page and click "Try Now"
2. Upload a plant leaf image
3. Receive general plant health guidance
4. Use the chat assistant for specific symptom-based diagnosis

## Example Chat Interactions

**User**: "My plant has yellow leaves starting from the bottom, what could be wrong?"

**AI**: "Yellow leaves starting from the bottom typically indicate overwatering or natural aging. Check if the soil is soggy - if so, reduce watering frequency and ensure good drainage. If soil is appropriate, this might be normal leaf drop. What type of plant is it, and how often do you water?"

## API Endpoints

- `GET /` - Main landing page
- `GET /trynow` - Image upload and analysis page
- `POST /analyze` - Process uploaded plant image (returns general guidance)
- `POST /chat` - Chat with AI plant expert

## Technical Details

- **Backend**: Flask (Python)
- **AI Provider**: Groq (llama-3.1-8b-instant for chat, llama-3.3-70b-versatile as fallback)
- **Image Processing**: PIL (Pillow) for image handling
- **Frontend**: HTML, CSS, JavaScript

## Supported Image Formats

- PNG, JPG, JPEG, GIF, BMP, WebP
- Maximum recommended size: 5MB
- Images are processed for optimal handling

## Getting the Best Results

### For Plant Diagnosis:
1. **Use the Chat Assistant** - Describe symptoms in detail
2. **Include Plant Type** - "My tomato plant..." or "My houseplant..."
3. **Describe Symptoms** - Color changes, spots, wilting, location on plant
4. **Mention Care Routine** - Watering frequency, light conditions, recent changes

### Example Good Descriptions:
- "My fiddle leaf fig has brown spots with yellow halos on older leaves"
- "White powdery substance appeared on my rose bush leaves after humid weather"
- "Tomato plant leaves are curling upward and turning yellow from bottom up"

## Error Handling

The application includes comprehensive error handling for:
- Missing or invalid API keys
- Network connectivity issues
- API rate limits
- Invalid file formats

## Environment Variables

- `GROQ_API_KEY` - Your Groq API key (required)

## License

This project is open source and available under the MIT License.



