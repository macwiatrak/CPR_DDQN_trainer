from environment import *

for c in range(100):
    env = GameEnv()
    s = env.reset()

    #env.render_env()
    i = 0
    agent1_reward = 0
    agent2_reward = 0
    agent3_reward = 0
    agent4_reward = 0

    #while True:
    for i in range(1000):
        #env.render_env()
        #plt.imshow(temp)
        #plt.show(block=False)
        #plt.pause(0.01)
        #plt.clf()
        action1 = np.random.randint(8)
        action2 = np.random.randint(8)
        action3 = np.random.randint(8)
        action4 =  np.random.randint(8)
        action_n = [action1, action2, action3, action4]

        rew_n, obs_n, done, untagged = env.step(action_n)
        #env.step(action_n)
        #if done == True:
         #   env.reset()
        i += 1
        agent1_reward += rew_n[0]
        agent2_reward += rew_n[1]
        agent3_reward += rew_n[2]
        agent4_reward += rew_n[3]

        #print(i, 'agent1_obs:', obs_n[0].shape, 'agent2_obs:', obs_n[1].shape, 'agent3_obs:', obs_n[2].shape)
        #if rew_n[0] or rew_n[1] or rew_n[2]:
         #   print(i, 'agent1 action: ', action1, 'agent2 action: ', action2, 'agent3 action: ', action3,)
            #print(i, 'agent1_obs:', obs_n[0])
            #print(i, 'agent1 reward: ', r1, 'agent2 reward', r2)
    print(i, 'agent1: ', agent1_reward, 'agent2: ', agent2_reward,
          'agent3: ', agent3_reward, 'agent4: ', agent4_reward)