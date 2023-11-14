# Import the PDDLReader and PDDLWriter classes
from unified_planning.io import PDDLReader, PDDLWriter
from unified_planning.shortcuts import *
from unified_planning.io.pddl_reader import nested_expr, CustomParseResults

# reader = PDDLReader()
# problem = reader.parse_problem('assignment-domain3.pddl', 'problem4.pddl')
# # print(problem)


# # with OneshotPlanner(name='popf') as planner:
# #     result = planner.solve(problem)
# #     if result.status == up.engines.PlanGenerationResultStatus.SOLVED_SATISFICING:
# #         print("plan: %s" % result.plan)
# #     else:
# #         print("No plan found.")



# types_map_str = {'robot': 'robot', 'person': 'person', 'crate': 'crate', 'location': 'location', 'content': 'content', 'carrier': 'carrier'}
# types_map = {}
# types = {}
# for k,v in types_map_str.items():
#     if k not in types:
#         types[k] = CaseInsensitiveToken(k)
#     if v not in types:
#         types[v] = CaseInsensitiveToken(v)
    
#     types_map[types[k]] = types[v]

# # print(f"types_map: {types_map}")

# reader = PDDLReader()
# goal = "(and (not (= (capacity carrier1) 0)))"
# # goal = "(have(p1, food) and have(p1, beverage) and have(p3, medicine) and have(p4, food) and have(p5, medicine) and have(p6, beverage))"
# problem_res = nested_expr().setResultsName("goal").parse_string(goal, parse_all=True)
# # expr = reader._parse_exp(problem, None, types_map, {}, problem_res["goal"][0])
# # expr = reader._parse_exp(problem, None, types_map, {}, goal)
# # print(expr)
# # print(type(expr))

# print(f"hierarchy: {problem.user_types_hierarchy}")
# for p,cc in problem.user_types_hierarchy.items():
#     p_name = 'Object'
#     if p is not None:
#         p_name = p.name
    
#     cc_name = None
#     if cc:
#         cc_name = ' '.join(c.name for c in cc)

#     print(p_name, '->', cc_name)

# types2 = {}
# types_map2 = {}
# # for p,cc in problem.user_types_hierarchy.items():
# #     if len(cc) == 0:
# #         tt = [[p.name, p.name]]
# #     else:
# #         tt = []
# #         for c in cc:
# #             tt.append([c.name, str(c)])
# #     print(tt)
# #     for tl,tr in tt:
# #         if tl not in types2:
# #             types2[tl] = CaseInsensitiveToken(tl)
# #         if tr not in types2:
# #             types2[tr] = CaseInsensitiveToken(tr)

# #         types_map2[types2[tl]] = types2[tr]

# for p,cc in problem.user_types_hierarchy.items():
#     if len(cc) > 0:
#         for c in cc:
#             # if c.name not in types2:
#             #     types2[c.name] = CaseInsensitiveToken(c.name)
#             # if str(c) not in types2:
#             #     types2[str(c)] = CaseInsensitiveToken(str(c))

#             # types_map2[types2[c.name]] = types2[str(c)]
#             types_map2[CaseInsensitiveToken(c.name)] = problem.user_type(c.name)

# print(types_map2)
# goalFNode = reader._parse_exp(problem, None, types_map2, {}, problem_res["goal"][0])
# print(goalFNode)
# problem.clear_goals()
# problem.add_goal(goalFNode)

# print(problem.goals[0].node_type)

problem = PDDLReader().parse_problem('assignment-domain3.pddl', 'assignment-problem3a.pddl')


types_map = {}
for tt in problem.user_types_hierarchy.values():
    if len(tt) > 0:
        for t in tt:
            types_map[t.name] = problem.user_type(t.name)

goal_exp = '(and (have p6 beverage))'
# goal_res = parse_string(set_results_name(nested_expr(), "goal"), goal_exp, parse_all=True)
goal_res = nested_expr().setResultsName("goal").parse_string(goal_exp, parse_all=True)
goal = CustomParseResults(goal_res["goal"][0])
print(f"CustomParseResults::{goal}")
goalFNode = PDDLReader()._parse_exp(problem, None, types_map, {}, goal, goal_exp)
print(f"goalFNode::{goalFNode}")
problem.add_goal(
    goalFNode
)
print(problem.goals[-1])