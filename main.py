from multiprocessing import Process, Pipe
import bot_test
import sanic_test

bot_test_pipe_end, sanic_test_pipe_end = Pipe()

sanicbot = Process(
        target = bot_test.main,
        args = (bot_test_pipe_end,)
        )

sanic = Process(
        target = sanic_test.main,
        args = (sanic_test_pipe_end,)
        )

sanicbot.start()
sanic.start()
sanicbot.join()
sanic.join()
