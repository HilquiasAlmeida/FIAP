import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:url_launcher/url_launcher.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Rastreamento Infantil',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const TrackingHomePage(),
    );
  }
}

class TrackingHomePage extends StatefulWidget {
  const TrackingHomePage({super.key});

  @override
  State<TrackingHomePage> createState() => _TrackingHomePageState();
}

class _TrackingHomePageState extends State<TrackingHomePage> {
  // ATENÇÃO: Substitua pelo IP do seu servidor onde o Flask (server.py) está rodando
  final String serverUrl = "http://192.168.1.100:5000/location";
  
  Map<String, dynamic> locationData = {
    "device_id": "Carregando...",
    "latitude": 0.0,
    "longitude": 0.0,
    "timestamp": "Aguardando...",
    "status": "Conectando..."
  };
  bool isLoading = false;

  Future<void> fetchLocation() async {
    setState(() { isLoading = true; });
    try {
      final response = await http.get(Uri.parse(serverUrl));
      if (response.statusCode == 200) {
        setState(() {
          locationData = json.decode(response.body);
        });
      }
    } catch (e) {
      setState(() {
        locationData["status"] = "Erro de conexão";
      });
    } finally {
      setState(() { isLoading = false; });
    }
  }

  Future<void> openMap(double lat, double lng) async {
    final Uri googleMapsUrl = Uri.parse("https://www.google.com/maps?q=$lat,$lng");
    if (!await launchUrl(googleMapsUrl, mode: LaunchMode.externalApplication)) {
      throw Exception('Não foi possível abrir o Google Maps.');
    }
  }

  @override
  void initState() {
    super.initState();
    fetchLocation();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Rastreamento Infantil IoT'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Center(
          child: Card(
            elevation: 4,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            child: Padding(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Center(
                    child: Text(
                      'Status da Criança ao Vivo',
                      style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                    ),
                  ),
                  const Divider(height: 30),
                  Text('Dispositivo: ${locationData["device_id"]}'),
                  const SizedBox(height: 10),
                  Text('Latitude: ${locationData["latitude"]}'),
                  const SizedBox(height: 10),
                  Text('Longitude: ${locationData["longitude"]}'),
                  const SizedBox(height: 10),
                  Text('Última Att: ${locationData["timestamp"]}'),
                  const SizedBox(height: 10),
                  Row(
                    children: [
                      const Text('Status: '),
                      Chip(
                        label: Text(
                          locationData["status"],
                          style: const TextStyle(color: Colors.white),
                        ),
                        backgroundColor: Colors.green,
                      ),
                    ],
                  ),
                  const SizedBox(height: 30),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton.icon(
                      onPressed: () => openMap(
                        locationData["latitude"], 
                        locationData["longitude"]
                      ),
                      icon: const Icon(Icons.map),
                      label: const Text('Abrir no Google Maps'),
                      style: ElevatedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 14),
                        backgroundColor: Colors.blue,
                        foregroundColor: Colors.white,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: fetchLocation,
        tooltip: 'Atualizar Posição',
        child: isLoading ? const CircularProgressIndicator(color: Colors.white) : const Icon(Icons.refresh),
      ),
    );
  }
}
