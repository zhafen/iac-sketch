import * as d3 from "d3";
import React, { useEffect, useRef } from "react";
import yaml from "yaml";

// const workflow = await d3.json("/workflow.json");
const resources = await d3.json("/resources.json");
const workflow = await d3.text("/workflow.yaml").then(data => yaml.parse(data));

// Parse the workflow to get the nodes and links
const nodes = [];
const links = [];
// Loop over entities
for (const entity of Object.keys(workflow)) {
  // Loop over components per entity
  for (const comp of workflow[entity]) {
    // Parse
    // If the component is just a string, that string is the type of the component
    if (typeof comp === "string") {
      var formatted_comp = { type: comp };
    // If the component is an object, it should have a single key,
    // which is the type of the component.
    // If the value is an object, then value is the component.
    } else if (typeof comp === "object" && Object.keys(comp).length === 1) {
      const comp_value = Object.values(comp)[0];
      const comp_key = Object.keys(comp)[0];
      if (typeof comp_value === "object") {
        var formatted_comp = { ...comp_value, type: comp_key };
      } else {
      // If the value is not an object, then the component consists of just the type
      // and a single field with the type as the key and the value as the value.
        var formatted_comp = { type: comp_key, comp_key: comp_value};
      }
    } else {
      throw new Error(`Unexpected component format in workflow. Entity: ${entity}, Component: ${JSON.stringify(comp)}`);
    }

    // Add task resources as nodes
    if (formatted_comp.type === "task") {
      nodes.push({
        id: entity,
      });
      // Parse flow resources
    } else if (formatted_comp.type === "flow") {
      for (const edge of formatted_comp.edges.split("\n")) {
        // Skip empty lines
        if (edge.trim() === "") continue;

        // Get the source and target nodes
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

export default function ForceDirectedGraph() {

  const width = window.innerWidth;
  const height = window.innerHeight;

  const containerStyle = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
  };

  const svgRef = useRef();

  useEffect(() => {
    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove(); // Clear previous content

    const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id(d => d.id).distance(100))
      .force("charge", d3.forceManyBody().strength(-300))
      .force("center", d3.forceCenter(width / 2, height / 2));

    const marker = svg.append("defs").append("marker")
      .attr('id', 'arrow')
      .attr("fill-opacity", 0.6)
      .attr('viewBox', '0 0 30 10')
      .attr('refX', 30)
      .attr('refY', 5)
      .attr('markerWidth', 30)
      .attr('markerHeight', 10)
      .attr('markerUnits', 'userSpaceOnUse')
      .attr('orient', 'auto')
      .append('path')
      .attr('d', 'M 0 0 L 30 5 L 0 10 Z');

    const link = svg.append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke-width", 5)
      .attr("marker-end", "url(#arrow)");

    const node = svg.append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("r", 5)
      .attr("fill", d => d3.schemeCategory10[d.group % 10])
      .call(drag(simulation));

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

  return (
    <div style={containerStyle}>
      <svg ref={svgRef} width={width} height={height}></svg>
    </div>
  );
}