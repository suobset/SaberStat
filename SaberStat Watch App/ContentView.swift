//
//  ContentView.swift
//  SaberStat Watch App
//
//  Created by Kush on 11/27/23.
//

import SwiftUI
import WatchConnectivity

struct ContentView: View {
    @State private var isPlaying = false
    @State private var hits = 0
    @State private var misses = 0
    @State private var roundData: (hits: Int, misses: Int)?

    var body: some View {
        VStack {
            // Display Hits/Misses during an ongoing round
            if isPlaying {
                Text("Hits: \(hits) Misses: \(misses)")
            }

            // Play/Pause Button
            Button(action: {
                if isPlaying {
                    // Stop the round and send data to iPhone
                    stopRound()
                } else {
                    // Start a new round
                    startRound()
                }
            }) {
                Text(isPlaying ? "Stop Battle" : "Start Battle")
            }
            .padding()
        }
    }

    private func startRound() {
        isPlaying = true
        hits = 0
        misses = 0

        // Start your logic to track hits and misses during the round
        // You might use the accelerometer or other sensors to detect hits/misses

        // For demo purposes, simulate hits and misses
        simulateHitsAndMisses()
    }

    private func stopRound() {
        isPlaying = false
        roundData = (hits, misses)

        // Send data to iPhone
        sendDataToiPhone()

        // Reset hits and misses for the next round
        hits = 0
        misses = 0
    }

    private func sendDataToiPhone() {
        guard WCSession.default.isReachable else {
            print("iPhone is not reachable.")
            return
        }

        // Prepare the data to be sent to iPhone
        let roundDataDictionary: [String: Any] = ["hits": hits, "misses": misses]

        // Send the data
        WCSession.default.sendMessage(roundDataDictionary, replyHandler: { response in
            // Handle any response from the iPhone if needed
        }, errorHandler: { error in
            print("Error sending data to iPhone: \(error.localizedDescription)")
        })
    }

    private func simulateHitsAndMisses() {
        // For demo purposes, simulate hits and misses during the round
        // You might replace this with your actual logic for detecting hits and misses
        Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { timer in
            if Bool.random() {
                self.hits += 1
            } else {
                self.misses += 1
            }

            // Update the UI during an ongoing round
            if isPlaying {
                // Update UI on the main thread
                DispatchQueue.main.async {
                    // Update the UI to display hits and misses dynamically
                    // This is just a basic example; adjust based on your UI structure
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
