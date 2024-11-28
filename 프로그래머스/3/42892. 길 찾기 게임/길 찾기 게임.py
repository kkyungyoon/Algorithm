import sys
sys.setrecursionlimit(10000)

def solution(nodeinfo):
    nodes = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]

    # y값 기준 내림차순, x값 기준 오름차순 정렬
    nodes.sort(key=lambda node: (-node[2], node[1]))

    # 이진 트리 구성 함수
    def build_tree(nodes):
        if not nodes:
            return None
        root = nodes[0] # 정렬 후이므로, 0번째가 root
        left_nodes = [node for node in nodes if node[1] < root[1]]  # root 노드 기준 왼쪽
        right_nodes = [node for node in nodes if node[1] > root[1]]  # root 노드 기준 오른쪽
        return (root, build_tree(left_nodes), build_tree(right_nodes))  # 현재 노드와 서브트리 반환

    # 전위 순회 함수
    def preorder(node):
        if not node:
            return []
        root, left, right = node
        return [root[0]] + preorder(left) + preorder(right)

    # 후위 순회 함수
    def postorder(node):
        if not node:
            return []
        root, left, right = node
        return postorder(left) + postorder(right) + [root[0]]

    # 트리 구성
    tree = build_tree(nodes)

    # 전위 및 후위 순회 결과 반환
    return [preorder(tree), postorder(tree)]
