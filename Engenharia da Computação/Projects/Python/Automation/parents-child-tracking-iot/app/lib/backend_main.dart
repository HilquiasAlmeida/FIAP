import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:url_launcher/url_launcher.dart';

class ApiService {
  // ATENÇÃO: Substitua pelo IP do seu servidor onde o Flask (server.py) está rodando
  static const String serverUrl = "http://192.168.1.100:5000/location";

  // Método que busca a localização no backend Python/PostgreSQL
  static Future<Map<String, dynamic>> fetchLocation() async {
    try {
      final response = await http.get(Uri.parse(serverUrl));
      if (response.statusCode == 200) {
        return json.decode(response.body);
      }
    } catch (e) {
      print("Erro ao conectar com o backend: $e");
    }
    return {
      "device_id": "Desconectado",
      "latitude": 0.0,
      "longitude": 0.0,
      "timestamp": "-",
      "status": "Erro de conexão"
    };
  }

  // Método que aciona o aplicativo nativo do Google Maps
  static Future<void> openMap(double lat, double lng) async {
    final Uri googleMapsUrl = Uri.parse("https://www.google.com/maps?q=$lat,$lng");
    if (!await launchUrl(googleMapsUrl, mode: LaunchMode.externalApplication)) {
      throw Exception('Não foi possível abrir o Google Maps.');
    }
  }
}
