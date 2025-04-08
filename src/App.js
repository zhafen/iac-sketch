import * as d3 from "d3";
import React, { useEffect, useRef } from "react";
import yaml from "yaml";

// const workflow = await d3.json("/workflow.json");
const resources = await d3.json("/resources.json");
const workflow = await d3.text("/workflow.yaml").then(data => yaml.parse(data));

// Parse the workflow to get the nodes and links
const nodes = [];
const links = [];
for (const key of Object.keys(workflow)) {
  for (const item of workflow[key]) {
    // Add task resources as nodes
    if (item.r === "task") {
      nodes.push({
        id: key,
      });
    // Parse flow resources
    } else if (item.r === "flow") {
      for (const edge of item.edges.split("\n")) {
        if (edge.trim() === "") continue; // Skip empty lines
        const [source, target] = edge.split(" --> ");
        links.push({
          source: source,
          target: target,
          value: 1,
        });
      }
    }
  }
}

// const data = {
// nodes: [
// { id: "node1", group: 1 },
// { id: "node2", group: 1 },
// { id: "node3", group: 1 },
// ],
// links: [
// { source: "node1", target: "node2", value: 1 },
// { source: "node1", target: "node3", value: 10 },
// ],
// }

export default function ForceDirectedGraph({ width = 640, height = 400 }) {
  const svgRef = useRef();

  useEffect(() => {
    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove(); // Clear previous content

    const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id).distance(100))
      .force("charge", d3.forceManyBody().strength(-300))
      .force("center", d3.forceCenter(width / 2, height / 2));

    const link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke-width", d => Math.sqrt(d.value));

    const node = svg.append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("r", 5)
      .attr("fill", d => d3.schemeCategory10[d.group % 10])
      .call(drag(simulation));

    node.append("title")
      .text(d => d.id);

    simulation.on("tick", () => {
      link
        .attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

      node
        .attr("cx", d => d.x)
        .attr("cy", d => d.y);
    });

    function drag(simulation) {
      function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      }

      function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
      }

      function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }

      return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
    }
  }, [width, height]);

  return <svg ref={svgRef} width={width} height={height}></svg>;
}