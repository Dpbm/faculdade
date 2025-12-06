import matplotlib.pyplot as plt
import pandas as pd
import random

# import ran
import rand


if __name__ == "__main__":
    # print(ran.add(1,1))
    #print(rand.cpp_seed())
    k = 1000000
    python_seeds = random.sample(list(range(-100000, 9999999)), k=k)
    cpp_seeds = [ rand.cpp_seed() for _ in range(k)]
    
    results_python_default = []
    results_python_seed = []
    results_cpp = []
    results_cpp_inc = []
    
    """
       shot_begin[i] = num_shots * i / distributed_procs_;
       shot_end[i] = num_shots * (i + 1) / distributed_procs_; 
    """

    shot_begin = 0
    shot_end = k

    """
      uint_t num_local_shots =
      shot_end[distributed_rank_] - shot_begin[distributed_rank_];
    """

    num_local_shots = k


    """
        i_shot = num_local_shots * i / par_shots;
        e_shot = num_local_shots * (i + 1) / par_shots;
    """

    par_shots = 2
    
    i_shot = num_local_shots 

    for i in range(k):
        results_python_default.append(random.choice([0,0,1]))

    for i in range(k):
        random.seed(python_seeds[i])
        results_python_seed.append(random.choice([0,0,1]))

        random.seed(cpp_seeds[i])
        results_cpp.append(random.choice([0,0,1]))

    for i in range(k):
        """
            i_shot = num_local_shots * i / par_shots;
            e_shot = num_local_shots * (i + 1) / par_shots;
        """

        
        random.seed(shot_begin+i)
        results_cpp_inc.append(random.choice([0,0,1]))

    data = pd.DataFrame({"cpp":results_cpp, "cpp_inc":results_cpp_inc,"python_seed":results_python_seed, "python_default":results_python_default})
    results = pd.DataFrame(columns=("cpp", "python_seed", "python_default", "cpp_inc"))
    results["cpp"] = data["cpp"].value_counts()
    results["cpp_inc"] = data["cpp_inc"].value_counts()
    results["python_seed"] = data["python_seed"].value_counts()
    results["python_default"] = data["python_default"].value_counts()


    plt.figure(figsize=(20,10))
    plt.subplot(2,2,1)
    plt.title("CPP")
    plt.bar(x=[0,1], height=results["cpp"])
    
    plt.subplot(2,2,2)
    plt.title("CPP INCREMENT")
    plt.bar(x=[0,1], height=results["cpp_inc"])

    plt.subplot(2,2,3)
    plt.title("PYTHON DEFAULT")
    plt.bar(x=[0,1], height=results["python_default"])

    plt.subplot(2,2,4)
    plt.title("PYTHON WITH SEEDS")
    plt.bar(x=[0,1], height=results["python_seed"])

    plt.savefig("test.png")


    
