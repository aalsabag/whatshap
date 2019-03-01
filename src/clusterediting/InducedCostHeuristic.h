#ifndef INDUCEDCOSTHEURISTICLIGHT_H
#define INDUCEDCOSTHEURISTICLIGHT_H

#include "EdgeHeap.h"
#include "ClusterEditingSolutionLight.h"

class InducedCostHeuristic {


public:
    InducedCostHeuristic(StaticSparseGraph& param_graph, bool param_bundleEdges);
    ClusterEditingSolutionLight solve();

private:    
    void init();
    bool resolvePermanentForbidden();
    void setForbidden(const StaticSparseGraph::Edge e);
    void setPermanent(const StaticSparseGraph::Edge e);
    
    /**
    * Updates icf and icp for the edge uw under the assumption that edge uv will be set to forbidden.
    */
    void updateTripleForbiddenUW(const StaticSparseGraph::EdgeWeight uv, const StaticSparseGraph::Edge uw, const StaticSparseGraph::EdgeWeight vw);

    /**
    * Updates icf and icp for the edge uw under the assumption that edge uv will be set to permanent.
    */
    void updateTriplePermanentUW(const StaticSparseGraph::EdgeWeight uv, const StaticSparseGraph::Edge uw, const StaticSparseGraph::EdgeWeight vw);
    
    bool bundleEdges;
    StaticSparseGraph graph;
    EdgeHeap edgeHeap;
    StaticSparseGraph::EdgeWeight totalCost;
};

#endif // INDUCEDCOSTHEURISTICLIGHT_H