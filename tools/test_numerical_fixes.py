"""Synthetic checks; never import or run whole coursework scripts."""
from pathlib import Path
import ast
import contextlib
import io
import unittest
import warnings
from types import SimpleNamespace
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.special import xlogy
from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[1]
FNA = "financial-numerical-analysis"
FE = "financial-engineering"
BDFC = "big-data-financial-computing"

def functions(path):
    tree=ast.parse((ROOT/path).read_text(encoding="utf-8"))
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef)]
    env={"np":np,"chi2":chi2,"xlogy":xlogy}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),path,"exec"),env)
    return env

class NumericalFixes(unittest.TestCase):
    def test_gaussian_integer_fractional_and_pivot_cases(self):
        for file in ("exercise-01.py","exercise-03.py"):
            solve=functions(f"{FNA}/assignment-08/{file}")["Equation_GEPivot"]
            for A,b in [
                (np.array([[2,1,-1,2],[4,4,1,3],[-6,-1,10,10],[-2,1,8,4]]),np.array([[2],[4],[-5],[1]])),
                (np.array([[2,1],[1,1]]),np.array([[1],[0]])),
                (np.array([[0.,1],[2,3]]),np.array([[1.],[4]])),
            ]:
                with self.subTest(file=file),contextlib.redirect_stdout(io.StringIO()):
                    x=solve(A,b)
                    np.testing.assert_allclose(x,np.linalg.solve(A,b),atol=1e-12)
                    np.testing.assert_allclose(A@x,b,atol=1e-12)

    def test_jacobi_equal_norm_false_stop(self):
        A=np.array([[1.,2,0],[0,1,2],[0,0,1]])
        for file in ("exercise-01.py","exercise-03.py"):
            solve=functions(f"{FNA}/assignment-09/{file}")["jacobi_iteration"]
            np.testing.assert_allclose(solve(A,np.ones((3,1)),1e-10),[[3.],[-1],[1]],atol=1e-10)

    def test_iterations_latest_residual_and_finite_failure(self):
        A=np.array([[3.,-1,1],[1,3,1],[1,2,7]])
        b=np.array([[7.],[-3],[11]])
        for file,names in [("exercise-01.py",["jacobi_iteration"]),("exercise-02.py",["GaussSeidel_iteration"]),("exercise-03.py",["jacobi_iteration","GaussSeidel_iteration"])]:
            env=functions(f"{FNA}/assignment-09/{file}")
            for name in names:
                with self.subTest(file=file,name=name):
                    x=env[name](A,b,1e-10)
                    self.assertLessEqual(np.linalg.norm(A@x-b,np.inf),1e-10)
                    np.testing.assert_allclose(x,np.linalg.solve(A,b),atol=1e-10)
                    with self.assertRaises(RuntimeError):
                        env[name](np.array([[1.,2],[2,1]]),np.ones((2,1)),1e-12,max_iter=5)
                    with self.assertRaises(ValueError):
                        env[name](np.array([[0.,1],[1,1]]),np.ones((2,1)),1e-12)

    def test_both_actual_hedge_regression_blocks(self):
        tree=ast.parse((ROOT/FE/"assignment-01/sample_01.py").read_text(encoding="utf-8"))
        f=np.linspace(-.02,.02,20)
        noise=np.sin(np.arange(20));noise-=noise.mean();noise-=np.dot(noise,f)/np.dot(f,f)*f
        portfolio=2*f+.001*noise
        env={"np":np,"sm":sm,"return_stock":pd.DataFrame({"portfolio":portfolio}),"return_futures":pd.DataFrame({"IF":f,"IH":f*.5,"IC":f*1.1,"IM":f*1.2}),"i":0,"best_futures_index":0}
        loop=next(n for n in tree.body if isinstance(n,ast.For) and "return_futures.shape" in ast.unparse(n.iter))
        nodes=[n for n in loop.body if isinstance(n,ast.Assign)][:5]
        exec(compile(ast.Module(body=nodes,type_ignores=[]),"<hedge-loop>","exec"),env)
        self.assertAlmostEqual(float(env["results"].params.iloc[1]),2.0,places=12)
        start=next(i for i,n in enumerate(tree.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="best_futures_index" for t in n.targets))
        nodes=[]
        for n in tree.body[start+1:]:
            if isinstance(n,ast.Assign):
                nodes.append(n)
                if any(isinstance(t,ast.Name) and t.id=="best_beta" for t in n.targets):break
        exec(compile(ast.Module(body=nodes,type_ignores=[]),"<hedge-final>","exec"),env)
        h=np.cov(portfolio,f,ddof=0)[0,1]/np.var(f)
        self.assertAlmostEqual(float(env["best_beta"]),2.0,places=12)
        self.assertAlmostEqual(float(env["best_beta"]),h,places=12)
        for other in (h-.1,h+.1):self.assertLess(np.var(portfolio-h*f),np.var(portfolio-other*f))

    def test_var_zero_all_alternating_and_mixed_exceedances(self):
        for file,ai in [("homework_08_test.py",False),("ai-assisted/homework_08.py",True)]:
            env=functions(f"{BDFC}/assignment-08/{file}")
            for seq in [np.zeros(20,dtype=int),np.ones(20,dtype=int),np.array([0,1]*10),np.array([0,0,1,1]*5)]:
                r=-2*seq.astype(float) if ai else 2*seq.astype(float)
                with self.subTest(file=file,N=int(seq.sum())):
                    result=env["myfun_Kupiec"](r,np.ones(20),.05)
                    n=seq.sum();T=len(seq);p=n/T
                    expected=2*(xlogy(T-n,1-p)+xlogy(n,p)-xlogy(T-n,.95)-xlogy(n,.05))
                    self.assertTrue(np.isfinite(result[0]))
                    self.assertAlmostEqual(result[0],expected,places=12)
                    self.assertTrue(0<=result[1]<=1)
                    ind=env["myfun_Christoffersen"](r,np.ones(20))
                    if n in (0,T):self.assertTrue(np.isnan(ind[0]))
                    else:
                        self.assertTrue(np.isfinite(ind[0]));self.assertGreaterEqual(ind[0],0);self.assertTrue(0<=ind[1]<=1)
            with self.assertRaises(ValueError):env["myfun_Kupiec"](np.array([]),np.array([]),.05)
            with self.assertRaises(ValueError):env["myfun_Kupiec"](np.ones(2),np.ones(2),0)

    def test_lppls_fit_and_plot_time_variable(self):
        tree=ast.parse((ROOT/FNA/"assignment-08/exercise-04.py").read_text(encoding="utf-8"))
        expr=next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="y_show" for t in n.targets))
        env={"np":np,"x":np.array([[1.],[-.2],[.4],[.1]]),"w":6.1023,"x_show_t":np.array([20.,50.,100.]),"x_show_tc_t":np.array([278.,248.,198.])}
        tau=env["x_show_tc_t"];env["x_show_t_m"]=tau**.2932
        actual=eval(compile(ast.Expression(expr),"<plot>","eval"),env)
        expected=1-.2*tau**.2932+.4*tau**.2932*np.cos(env["w"]*np.log(tau))+.1*tau**.2932*np.sin(env["w"]*np.log(tau))
        np.testing.assert_allclose(actual,expected)

    def test_three_month_winner_keeps_the_winner_stock(self):
        path=ROOT/BDFC/"assignment-02/homework_02_03/homework_02_effect.py"
        tree=ast.parse(path.read_text(encoding="utf-8"))
        call=next(n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and isinstance(n.func.value,ast.Name) and n.func.value.id=="max_return_3")
        data=pd.DataFrame({"winner":[0,0,0,.1,.2,.3],"loser":[0,0,0,-.4,-.3,-.2]})
        env={"data":data,"i":2,"max_code":"winner","min_code":"loser","max_return_3":[]}
        eval(compile(ast.Expression(call),"<winner-holding-return>","eval"),env)
        self.assertAlmostEqual(env["max_return_3"][0],1.1*1.2*1.3-1,places=12)

    def test_actual_month_end_aggregation_expression(self):
        path=ROOT/BDFC/"assignment-02/homework_02_multi.py"
        tree=ast.parse(path.read_text(encoding="utf-8"))
        expr=next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="data_matrix_monthly" for t in n.targets))
        values={"date":pd.to_datetime(["2025-01-30","2025-01-31","2025-02-03"]),"rf":[.01,.02,.03],"rm":[.1,.2,.3]}
        for code in ["600021","000021","600521","601021","600621","603021","688021","603221"]:
            values["return"+code]=[.1,.2,.3]
        result=eval(compile(ast.Expression(expr),"<month-end>","eval"),{"pd":pd,"data_matrix":pd.DataFrame(values)})
        self.assertEqual(list(result.index),list(pd.to_datetime(["2025-01-31","2025-02-28"])))
        self.assertAlmostEqual(result.iloc[0]["rf"],1.01*1.02-1)
        self.assertAlmostEqual(result.iloc[0]["rm"],.3)
        self.assertAlmostEqual(result.iloc[1]["return600021"],.3)

    def test_all_eight_solver_results_are_explicit_scalars(self):
        path=ROOT/FE/"assignment-04/sample_04.py"
        tree=ast.parse(path.read_text(encoding="utf-8"))
        assignments=[n for n in ast.walk(tree) if isinstance(n,ast.Assign) and "optimize.fsolve" in ast.unparse(n.value)]
        self.assertEqual(len(assignments),8)
        for n in assignments:
            env={"optimize":SimpleNamespace(fsolve=lambda function,initial:np.array([.2])),
                 "myfun_call":None,"myfun_put":None,"sigma_0":.3,"sigma_call_5":np.zeros(1),"sigma_put_5":np.zeros(1),"i":0}
            with warnings.catch_warnings():
                warnings.simplefilter("error",DeprecationWarning)
                exec(compile(ast.Module(body=[n],type_ignores=[]),"<scalar-result>","exec"),env)
            target=n.targets[0].value.id
            self.assertEqual(env[target][0],.2)

    def test_fama_macbeth_parameter_positions_with_pandas_labels(self):
        path=ROOT/BDFC/"assignment-03/fama-macbeth/homework_03_FM.py"
        tree=ast.parse(path.read_text(encoding="utf-8"))
        expected=np.array([1.,2.,3.,4.])
        X=sm.add_constant(np.random.default_rng(2).normal(size=(20,3)))
        results=sm.OLS(pd.DataFrame({"return":X@expected}),X).fit()
        names=("const_list","size_list","ep_list","beta_list")
        env={"results":results,**{name:[] for name in names}}
        calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=="append" and isinstance(n.func.value,ast.Name) and n.func.value.id in names]
        self.assertEqual(len(calls),4)
        for call in calls:eval(compile(ast.Expression(call),"<Fama-MacBeth-parameter>","eval"),env)
        np.testing.assert_allclose([env[name][0] for name in names],expected,atol=1e-12)

if __name__=="__main__":
    with contextlib.redirect_stdout(io.StringIO()):
        unittest.main()
