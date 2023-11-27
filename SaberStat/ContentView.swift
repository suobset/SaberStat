//
//  ContentView.swift
//  SaberTest
//
//  Created by Kush on 11/26/23.
//

import SwiftUI

struct ContentView: View {
    // Dummy data for hits and misses in the range of 1-5
    let hitsData: [Double] = [4, 2, 5, 1, 3, 5, 4]
    let missesData: [Double] = [2, 1, 1, 3, 5, 4, 3]

    @State private var showHitsGraph = true

    var body: some View {
        NavigationView {
            VStack {
                // Bar Graph for hits or misses
                BarGraphView(data: showHitsGraph ? hitsData : missesData, color: showHitsGraph ? .green : .red, title: showHitsGraph ? "Hits" : "Misses")
                    .frame(height: 200)

                // Divider line
                Divider()

                // Log for hits and misses
                LogView(hits: hitsData, misses: missesData)
                    .padding()
                // Toggle between hits and misses graph
                Toggle("Toggle Graphs (Hits or Miss)", isOn: $showHitsGraph)
                    .padding()
            }
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .principal) {
                    VStack {
                        Text("SaberStat")
                            .font(.largeTitle)
                            .foregroundColor(.black)
                            .frame(maxWidth: .infinity, alignment: .center)
                    }
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

// BarGraphView: Displays a bar graph for hits or misses
struct BarGraphView: View {
    let data: [Double]
    let color: Color
    let title: String

    var body: some View {
        VStack {
            Text(title)
                .font(.headline)
                .padding(.bottom, 5)

            GeometryReader { geometry in
                HStack(alignment: .bottom, spacing: 10) {
                    ForEach(0..<data.count, id: \.self) { index in
                        BarView(value: data[index], color: color, maxYValue: 5)
                            .frame(width: (geometry.size.width - CGFloat(data.count * 10)) / CGFloat(data.count))
                    }
                }
            }
        }
    }
}

// BarView: Represents a bar in the graph
struct BarView: View {
    let value: Double
    let color: Color
    let maxYValue: Double

    var body: some View {
        VStack {
            Spacer()

            RoundedRectangle(cornerRadius: 5)
                .fill(color)
                .frame(height: CGFloat(value / maxYValue * 100))
        }
    }
}

// LogView: Displays a simple log of hits and misses
struct LogView: View {
    let hits: [Double]
    let misses: [Double]

    var body: some View {
        VStack(alignment: .leading) {
            Text("Log:")
                .font(.headline)
                .padding(.bottom, 5)

            ForEach(0..<min(hits.count, misses.count), id: \.self) { index in
                HStack {
                    Text("Round \(index + 1):")
                    Spacer()
                    Text("Hits: \(Int(hits[index])) Misses: \(Int(misses[index]))")
                }
                .padding(.bottom, 5)
            }
        }
    }
}
