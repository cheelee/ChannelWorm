
# coding: utf-8

# #Validating an channel model IV curve with data from an experiment

# In[2]:

# Imports and preliminaries.  
import os,sys
import numpy as np

TEST_DIR = os.path.dirname(os.path.realpath(__file__))#os.path.pardir # Location of your ChannelWorm repo
CW_HOME = os.path.dirname(TEST_DIR)
print(CW_HOME)
sys.path.insert(1,CW_HOME)

from channelworm.fitter import initiators



# ##Compare the IV curve predicted from the channel model to that observed from the data

# In[3]:

from neuronunit.tests.channel import IVCurvePeakTest
from neuronunit.models.channel import ChannelModel
# Warning message comes from NeuroTools, soon to be replaced by Elephant.  Ignore.  


# In[4]:

# Instantiate the model
# Instantiate the model
channel_model_name = 'EGL-19.channel'
channel_id = 'ca_boyle'
channel_file_path = os.path.join(CW_HOME,'models','%s.nml' % channel_model_name)

model = ChannelModel(channel_file_path,channel_index=0,name=channel_model_name)


# In[5]:

# Get the experiment data and instantiate the test
data_name = 'egl-19-IClamp-IV'
csv_path = os.path.join(CW_HOME,'channelworm','fitter','examples','egl-19-data','%s.csv' % data_name)
ref = {'fig':'2B','doi':'10.1083/jcb.200203055'}
x_var = {'type':'Voltage','unit':'V','toSI':1}
y_var = {'type':'Current','unit':'A/F','toSI':1}
IV = {'ref':ref,'csv_path':csv_path,'x_var':x_var,'y_var':y_var}
user_data = {'samples': {'IV': IV}}
myInitiator = initiators.Initiator(user_data)
sample_data = myInitiator.get_sample_params()
i_obs,v_obs = [np.array(sample_data['IV'][_]) for _ in ('I','V')] # Current in pA and membrane potential in V.  
observation = {'i':i_obs, 'v':v_obs}

test = IVCurvePeakTest(observation)


# In[6]:

# Judge the model output against the experimental data
score = test.judge(model)
score.summarize()
print("The score was computed according to '%s' with raw value %s" % (score.description,score.value))


# In[7]:

rd = score.related_data

