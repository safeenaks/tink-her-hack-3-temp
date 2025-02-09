from django.shortcuts import render
from django.http import JsonResponse

# View to render the chatbot homepage
def chatbot_home(request):
    return render(request, 'home.html')

# View to handle chatbot response
def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get('message')  # Get message from the user
        response_message = get_farming_response(user_message)
        return JsonResponse({"response": response_message})
    return JsonResponse({"response": "Invalid request."})

# Function to return predefined answers to farming-related questions
def get_farming_response(user_input):
    # Simple predefined questions and answers
    farming_answers = {
        "How to grow tomatoes?": "To grow tomatoes, ensure they have plenty of sunlight and well-drained soil. Water them regularly.",
        "What is organic farming?": "Organic farming avoids synthetic chemicals and uses natural methods to grow crops.",
        "How to prevent pests in farming?": "Use natural pesticides like neem oil or introduce beneficial insects to control pests.",
        "What is the best fertilizer for tomatoes?": "A balanced fertilizer with equal amounts of nitrogen, phosphorus, and potassium works best for tomatoes."
    }

    # Return the answer if the question is predefined, else a fallback response
    return farming_answers.get(user_input, "Sorry, I don't have an answer for that question. Try asking something else.")
def get_farming_response(user_input):
    # Expanded predefined questions and answers
    farming_answers = {
        "hi":"Hello! How can i assist you today?",
        "How to grow tomatoes?": "To grow tomatoes, ensure they have plenty of sunlight and well-drained soil. Water them regularly.",
        "What is organic farming?": "Organic farming avoids synthetic chemicals and uses natural methods to grow crops.",
        "How to prevent pests in farming?": "Use natural pesticides like neem oil or introduce beneficial insects to control pests.",
        "What is the best fertilizer for tomatoes?": "A balanced fertilizer with equal amounts of nitrogen, phosphorus, and potassium works best for tomatoes.",
        "How do I plant carrots?": "Carrots prefer loose, well-drained soil. Sow the seeds about 1/4 inch deep and space them 2 inches apart.",
        "What is crop rotation?": "Crop rotation involves growing different types of crops in the same area in sequential seasons to prevent soil depletion.",
        "How do I water my plants efficiently?": "Water your plants in the early morning or evening to reduce evaporation. Consider drip irrigation for efficiency.",
        "What is companion planting?": "Companion planting is the practice of growing different crops together to improve growth, repel pests, and boost yields.",
        "How do I control weeds naturally?": "Mulching, hand weeding, and using vinegar or salt can help control weeds naturally without chemicals.",
        "What is agroforestry?": "Agroforestry is the practice of integrating trees and shrubs into agricultural land to improve biodiversity and soil health.",
        "How to grow potatoes?": "Plant seed potatoes in loose, well-drained soil and ensure they are spaced 12 inches apart. Keep them well-watered and mulched.",
        "How do I grow wheat?": "Plant wheat in a well-drained soil with good sunlight. It requires a cool growing season and should be harvested when the grains are hard.",
        "How to grow cucumbers?": "Cucumbers need full sunlight and well-drained soil. They should be spaced at least 12 inches apart and watered regularly.",
        "How do I fertilize my garden organically?": "Use compost, manure, fish emulsion, or other organic fertilizers to enrich the soil naturally.",
        "What is hydroponics?": "Hydroponics is a method of growing plants without soil by using mineral nutrient solutions in water.",
        "How to grow strawberries?": "Plant strawberries in a sunny area with well-drained soil. Space them about 18 inches apart and keep them watered.",
        "How can I improve soil quality?": "Add organic matter like compost, mulch, or cover crops to improve soil structure and fertility.",
        "What is permaculture?": "Permaculture is a design philosophy that mimics natural ecosystems to create sustainable agricultural practices.",
        "How to grow beans?": "Beans thrive in well-drained soil with plenty of sunlight. Plant them 1 inch deep and 2 inches apart, and keep them watered.",
        "How to prevent soil erosion?": "Use cover crops, mulching, and contour farming to prevent soil erosion caused by wind and water.",
        "What is agroecology?": "Agroecology is the study of ecological processes applied to agricultural production systems.",
        "How to grow peppers?": "Peppers need full sun and warm temperatures. Plant them in well-drained soil and space them 18 inches apart.",
        "How to grow lettuce?": "Lettuce prefers cooler temperatures and well-drained soil. It should be watered regularly to keep the soil moist.",
        "What are the benefits of composting?": "Composting enriches the soil, reduces waste, and provides plants with organic nutrients.",
        "How to protect plants from frost?": "Use row covers, mulch, or bring potted plants indoors during cold weather to protect them from frost.",
        "What is a greenhouse used for?": "A greenhouse provides controlled conditions for growing plants, protecting them from extreme weather and pests.",
        "How to grow herbs at home?": "Plant herbs like basil, thyme, or mint in well-drained soil and ensure they get plenty of sunlight.",
        "How do I make my own mulch?": "You can make mulch by shredding leaves, grass clippings, or wood chips and spreading them around your plants.",
        "What is intercropping?": "Intercropping is the practice of growing two or more crops in close proximity to improve productivity and reduce pests.",
        "How do I know when to harvest carrots?": "Carrots are ready to harvest when the roots are about 1 inch in diameter and have reached the desired length.",
        "What are the best crops for crop rotation?": "Legumes, root vegetables, and leafy greens are ideal for crop rotation as they help improve soil health.",
        "How to grow spinach?": "Spinach grows best in cool weather and needs well-drained soil. Space the seeds 1 inch apart and keep them watered.",
        "How do I build raised garden beds?": "You can build raised beds using wood, stone, or concrete blocks. Fill them with quality soil and compost.",
        "How to grow garlic?": "Plant garlic cloves in the fall, 2 inches deep and 4 inches apart. Garlic needs full sun and well-drained soil.",
        "How do I water my garden in hot weather?": "Water deeply at the base of plants during early morning or evening to reduce evaporation and keep the roots hydrated.",
        "What are natural ways to control pests?": "Use neem oil, garlic spray, or introduce beneficial insects like ladybugs to control garden pests naturally.",
        "How to plant onions?": "Plant onion sets 1 inch deep in well-drained soil and ensure they receive plenty of sunlight and water.",
        "How to grow broccoli?": "Broccoli prefers cool temperatures and rich, well-drained soil. It should be spaced 18 inches apart and watered regularly.",
        "How to build a compost bin?": "A simple compost bin can be made using wood, chicken wire, or plastic containers to hold organic waste and encourage decomposition.",
        "How to manage water use in farming?": "Use drip irrigation, rainwater harvesting, and proper water management techniques to conserve water on the farm.",
        "How to grow apples?": "Plant apple trees in well-drained soil with full sunlight. They require regular pruning and care to produce good fruit.",
        "What is the importance of pollination?": "Pollination is essential for fruit and seed production. Bees and other pollinators help plants reproduce by transferring pollen.",
        "How to prevent overwatering?": "Ensure good drainage in your soil and use a moisture meter to check if the soil is too wet before watering again.",
        "What are cover crops used for?": "Cover crops are planted to protect the soil from erosion, improve soil fertility, and provide habitat for beneficial insects.",
        "How do I grow cauliflower?": "Cauliflower prefers cooler weather. Plant in well-drained soil, space them 18 inches apart, and keep them watered.",
        "How to improve farm biodiversity?": "Introduce a variety of crops, rotate crops, and conserve natural habitats to improve biodiversity on the farm.",
        "What is the importance of mulching?": "Mulching helps conserve moisture, suppress weeds, and add organic matter to the soil.",
        "How to grow avocados?": "Avocados require well-drained, slightly acidic soil. They need plenty of sunlight and a warm climate to thrive.",
        "How do I store seeds for the next season?": "Store seeds in a cool, dry place in airtight containers to maintain their viability for the next planting season.",
        "How to deal with plant diseases?": "Use disease-resistant varieties, remove affected plants, and apply organic fungicides to prevent the spread of plant diseases.",
        "What are the benefits of rainwater harvesting?": "Rainwater harvesting helps reduce reliance on other water sources and provides water for irrigation and other farm needs."
    }

    # Return the answer if the question is predefined, else a fallback response
    return farming_answers.get(user_input, "Sorry, I don't have an answer for that question. Try asking something else.")
