# pytest-fixture

pytest fixtures offer dramatic improvements over the classic xUnit style of setup/teardown functions:

    - fixtures have explicit names and are activated by declaring their use from test functions, modules, classes or whole projects.

    - fixtures are implemented in a modular manner, as each fixture name triggers a fixture function which can itself use other fixtures.

    - fixture management scales from simple unit to complex functional testing, allowing to parametrize fixtures and tests according to configuration and component options, or to re-use fixtures across function, class, module or whole test session scopes.

    - teardown logic can be easily, and safely managed, no matter how many fixtures are used, without the need to carefully handle errors by hand or micromanage the order that cleanup steps are added.

## How to run example code

The example codes in this directory uses [Redis](https://redis.io/).

To run redis on local machine, you could run it on docker by using the provided [docker-compose file](./docker-compose.yml).

After running the docker image of Redis, you could run tests by using 'pytest -v'.
