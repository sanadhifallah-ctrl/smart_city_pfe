from app.ai.speech_to_texte import transcribe
from app.ai.text_normaliser import text_normalizer
from app.ai.information_extractor import extract_infomation

def process_audio_service(audio_file):
    text = transcribe(audio_file)

    clean_text = text_normalizer(text)

    data = extract_infomation(clean_text)

    return {
        "text": clean_text,
        "category": data["category"],
        "priority": data["priority"]
    }

def optimize_reports_service(reports):
    coordinates = extract_coordinates(reports)

    valid_coords = validate_coordinates(coordinates)

    optimized_route = run_route_optimizer(valid_coords)

    return optimized_route