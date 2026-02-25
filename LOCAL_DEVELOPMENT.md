# Local development

This guide provides instructions for setting up your environment to work against local changes in the project.

## Prerequisites

- Clone [cloudbeds/mfd](https://github.com/cloudbeds/mfd) locally
    - If you already have it cloned, ensure you have the latest changes to ensure all types are still correct.
- Install [openapi-generator](https://openapi-generator.tech/docs/installation) and make sure you can run it from the
  command line.

## The error

Let's assume you are working with this library and realize one of the types is wrong. I'll use `/getReservations` as an
example. So, you receive a response from the endpoint and pydantic throws an exception that it cannot map `propertyID`
because the type says it's an `int` but the response is actually a `str`.

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for GetReservationsResponseDataInner
reservationID
  Input should be a valid int [type=int, input_value='123', input_type=str]
    For further information visit https://errors.pydantic.dev/2.12/v/int_type
```

## Step 1. Make changes to MFD type definitions

### Locate the PHP source file

If you don't know your way around the project, start by looking at
the [router file](https://github.com/cloudbeds/mfd/blob/main/application/config/routes_api_v1_3.php). You can locate
that `/getReservations` is mapped like so:

```php
$route['api/v1.3/getReservation'] = 'api_v1_1/api_reservation/index';
```

Despite looking into the v1.3 routes, the actual endpoint is mapped to the v1.1 controller. You can, therefore, find the
file here: https://github.com/cloudbeds/mfd/blob/main/application/controllers/api_v1_1/Api_reservation.php. Find the
`reservations_get` method and check its type annotations.

```
...
* @apiSuccess {Object[]} data Details for the reservation queried
* @apiSuccess {Integer} data.propertyID Properties identifier
* @apiSuccess {String} data.reservationID Reservation's unique identifier
...
```

### Making changes

Now that you've located the endpoint and its return types, you can make the necessary changes. In this case, you'll
change the type annotation from `Integer` to `String`.

```
...
* @apiSuccess {Object[]} data Details for the reservation queried
* @apiSuccess {String} data.propertyID Properties identifier
* @apiSuccess {String} data.reservationID Reservation's unique identifier
...
```

### Generating openapi specs

At this point, you can generate the openapi specs. Navigate to the `mfd` project root and run:

```bash
$ ./bin/mfd apidoc
```

You should now see the changes reflected in the `public_accessa/api` docs directories. Check that the changes make
sense. While integer to string is a straight forward change, some other changes might not generate the openapi type
you'd expect. For example, `Object[]` is a special notation for assosiative arrays if they're following by a comment
that describes the key type.

## Step 2. Generate the client

Back to this repo. Make a change to [openapitools.json](openapitools.json) to point `inputSpec` to the `mfd` project
directory on your machine, e.g., if `mdf` is on a sibling directory to this project, we can change it to:

```
"inputSpec": "../mfd/public_accessa/api/v1.3/docs/cb-v1.3-openapi-3.0.1.yaml",
```

Make sure you **DO NOT** commit the change above. Now, you can generate the client like so (I've installed
`openapi-generator` globally via brew; your command might be slightly different):

```bash
$ openapi-generator generate -c openapitools.json
```

You should see a bunch of new and/or changed files in `git`, depending on the changes you made. Some files might be
unrelated to the changes you made in the `mfd` project. They are just changes from other people that are missing since
the library's last release.

## Step 3. Use the local client in your project

This step is highly dependent on your project setup. Let's assume a project with `pyproject.toml` and `uv`.

In your `pyproject.toml`, you need to add an override to point to the local repo.

```toml
[tool.uv.sources]
cloudbeds-pms-v1-3 = { path = "/path/to/cloudbeds-api-python", editable = true }
```

Then, run `uv sync` and you should see that `uv` reports using the local repo instead of the published one. Don't forget
to remove the override and re-sync `uv` when you're done.

## Step 4. Run your project

If you run the project outside `docker`, you should restart the uvicorn server to pick up the changes, e.g.:

```bash
set -a && source .env && set +a && PYTHONPATH=src uv run uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

If you run the project inside `docker`, you'll need to mount the local repo into the container, because `docker` won't
be able to find the "symlinked" dependency.

At this point you should be able to run your project and see the changes reflected. The type is fixed and you can
proceed with development.

## Step 5. Release your changes

Once you're done, you can submit a PR to `mfd` with the changed types. Make sure to ping any teams that come up via the
`CODEOWNERS` file.

Depending on the urgency of the changes, you have a few options on how or when to release a new version of the library:

- If the changes are urgent, release a new library version using the commit SHA of the PR. This is somewhat risky
  because reviewers may reject your changes.
- If the changes are not urgent, wait until the PR is merged and then release a new library version using SHA.
- You can also wait until `mfd` is released and use the latest version as a target for release.

Library versions are released
using [GitHub Actions](https://github.com/cloudbeds/cloudbeds-api-python/actions/workflows/publish.yaml). This workflow
accepts branch, tag, or SHA references to MFD. So, `main`, `v1.3.0`, or `123456789abcdef` are all valid references.

While you should not directly commit changes in the library itself (using the workflow action above is enough, as it
makes the updates to the repo), the action allows you to do so if you need to. Push the changes to a branch, get it
reviewed and merged, and then run the action by providing the new version number. In this case, it will simply release
the new version to PyPi.

Once you have the new library version, update your project's dependencies to use the new version.