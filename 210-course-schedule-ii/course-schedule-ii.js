/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(n, prereq) {
    const indegree = Array(n).fill(0)
    const adj = {}
    for(let i=0;i<n;i++){
        adj[i] = []
    }
    for(const [u,v] of prereq){
        adj[v].push(u)
        indegree[u]+=1
    }
    const q = []
    const res = []
    for(let i=0;i<n;i++){
        if(indegree[i]==0){
            q.push(i)
        }
    }
    while(q.length>0){
        const node = q.shift()
        res.push(node)
        for(let nei of adj[node]){
            indegree[nei]-=1
            if (indegree[nei]==0){
                q.push(nei)
            }
        }
    }
    return res.length == n? res:[]

};