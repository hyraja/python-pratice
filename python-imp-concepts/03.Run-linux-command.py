# method 1
----------
import subprocess

def execute_command(command):
        """function will run the linux command on python

        Args:
            command ([string]): [it should be taken one string]
        """
        try:
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            output, err = process.communicate()
            if process.returncode != 0:
                LOG.error(f'Error  on the command[{command}]')
                return err.decode()

            LOG.info(f'command executed successfully [{command}]')
            LOG.info(output.decode().strip())
            return output.decode().strip()
        except subprocess.CalledProcessError as e:
            LOG.error(e)
            
            
 #method 2
 ---------
 import os
 
 os.popen(f' any linux command').read()
 
 #method 3
 ---------
 import subprocess
 
 # cmd should be any linux command
 
 def exec_command(cmd):
    """function will run the linux command on python

    Args:
        cmd ([string]): [it should be taken one string]
    """

    process = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    if process.returncode != 0:
        LOG.error(f'Error on cmd [{cmd}]')
        LOG.error(process.stdout.decode())
        return
    LOG.info(process.stdout.decode())
