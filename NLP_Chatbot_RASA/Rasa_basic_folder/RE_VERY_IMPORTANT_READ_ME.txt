Two things need to be ensured for the bot to work correctly - 

1. Rather than using "rasa train core" use "rasa train -vv -dump-stories --force"

2. Wherever your rasa in installed in your system for eg for me it was - C:\Users\Dell\anaconda3\envs\myenv\Lib\site-packages\rasa\core\channels
Go to console.py and change DEFAULT_STREAM_READING_TIMEOUT_IN_SECONDS to 25 from 10. This increases the reading timeout limit.

Once these 2 steps are followed, the bot works wonderfully!

P.S. - These 2 steps were discussed with Swastik Nayak from Upgrad and he said that 
rather than installing new package versions,if a change in command does the job, 
just mention it while submitting the project.