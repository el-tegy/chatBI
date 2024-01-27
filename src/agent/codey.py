from langchain.chat_models import ChatVertexAI
from langchain.prompts import ChatPromptTemplate
import vertexai
from vertexai.preview.generative_models import GenerativeModel
def code_generation(query):
    """
    Generate a response based on the prompt using the Gemini Pro model.

    Args:
        query (str): The user's input/query.
        
    Returns:
        str: The generated response by the language model.
             (The model's response to the user's input.)
    """
    # Create an instance of the GenerativeModel with the Gemini Pro model
    gemini_pro_model = GenerativeModel("gemini-pro")

    # Generate content using the Gemini Pro model with the specified configuration
    model_response = gemini_pro_model.generate_content(
        query,
        generation_config={"temperature": 0.2}
    )

    # Extract and return the text content from the generated response
    return model_response.candidates[0].content.parts[0].text

