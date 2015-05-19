import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Main mn = new Main();
		
		try {
			BufferedReader buffReader = new BufferedReader(new FileReader(new File(args[0])));
			
			String line;
			
			while ((line = buffReader.readLine()) != null){
				Main.Graph graph = mn.new Graph(line.substring(1, line.length()-1).split("\\|"));
				System.out.println( mergeAll(graph).nodes.get(0).data);
				
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	
	
	private static Graph mergeUniques(Graph graph){
		boolean mergeFound = true;
		
		while (mergeFound){
			
			mergeFound = false;
			for (Node n : graph.nodes){
				if (n.neighbors.size() == 1){
					graph.mergeNodes(n, n.neighbors.get(0));
					mergeFound = true;
					break;
				}
			}
		}
		return graph;
	} 
	
	private static Graph mergeAll(Graph graph){
		Main mn = new Main();
		Graph newGraph = mergeUniques(graph);
		if (newGraph.nodes.size() == 1){
			return newGraph;
		}
		else{
			ArrayList<Node> temp;
			Node n;
			for (int i = 0; i < newGraph.nodes.size(); i++){
				n = newGraph.nodes.get(i);
				temp = n.neighbors;
				for (Node neighbor : temp){
					n.neighbors = new ArrayList<Node>();
					n.neighbors.add(neighbor);
					Graph tempGraph = mergeAll(mn.new Graph(newGraph));
					if (tempGraph.nodes.size() == 1){
						if (tempGraph.nodes.get(0).data.length() == tempGraph.textSize){
							return tempGraph;
						}
					}
				}
			}
		}
		return graph;
	}
	
	
	private class Node {
		
		public String data;
		
		public ArrayList<Node> merged = new ArrayList<Node>();
		
		public ArrayList<Node> neighbors = new ArrayList<Node>();
		
		public Node(String s){
			this.data = s;
			this.merged.add(this);
		}
	}
	
	private class Graph {
		
		public ArrayList<Node> nodes;
		public int pieceSize;
		public int textSize;
		
		public Graph(String[] pieces){
			this.pieceSize = pieces[0].length();
			this.textSize = this.pieceSize + pieces.length - 1;
			this.nodes = this.genGraph(pieces);
		}
		
		public Graph(Graph graph){
			this.nodes = new ArrayList<Node>(graph.nodes);
			this.textSize = graph.textSize;
			this.pieceSize = graph.pieceSize;
		}
	
		private ArrayList<Node> genGraph(String[] pieces){
			ArrayList<Node> nodes = new ArrayList<Node>();
			for (String s : pieces){
				nodes.add(new Node(s));
			}
			for (Node n : nodes){
				for (Node nb : nodes){
					
					if (!n.equals(nb)){
						
						if((n.data.substring(1, n.data.length()).equals(nb.data.substring(0, nb.data.length()-1)))){
							n.neighbors.add(nb);
						}
					}
				}
			}
			return nodes;
		}
		
		public void mergeNodes(Node n1, Node n2){
			
			n1.data = n1.data.substring(0, n1.data.length()-(this.pieceSize-1)) + n2.data;
			n1.merged.add(n2);
			n1.neighbors = new ArrayList<Node>();
			for (Node n : n2.neighbors){
				if (!n1.merged.contains(n)){
					n1.neighbors.add(n);
				}
			}
			
			this.nodes.remove(n2);
			
			for (Node n : this.nodes){
				n.neighbors.remove(n2);
			}			
		}
	}

}

