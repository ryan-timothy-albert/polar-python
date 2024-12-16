"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
import httpx
from polar_sdk import models, utils
from polar_sdk._hooks import (
    AfterErrorContext,
    AfterSuccessContext,
    BeforeRequestContext,
)
from polar_sdk.utils import RetryConfig, SerializedRequestBody, get_body_content
from typing import Callable, List, Mapping, Optional, Tuple
from urllib.parse import parse_qs, urlparse


class BaseSDK:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config

    def get_url(self, base_url, url_variables):
        sdk_url, sdk_variables = self.sdk_configuration.get_server_details()

        if base_url is None:
            base_url = sdk_url

        if url_variables is None:
            url_variables = sdk_variables

        return utils.template_url(base_url, url_variables)

    def build_request_async(
        self,
        method,
        path,
        base_url,
        url_variables,
        request,
        request_body_required,
        request_has_path_params,
        request_has_query_params,
        user_agent_header,
        accept_header_value,
        _globals=None,
        security=None,
        timeout_ms: Optional[int] = None,
        get_serialized_body: Optional[
            Callable[[], Optional[SerializedRequestBody]]
        ] = None,
        url_override: Optional[str] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Request:
        client = self.sdk_configuration.async_client
        return self.build_request_with_client(
            client,
            method,
            path,
            base_url,
            url_variables,
            request,
            request_body_required,
            request_has_path_params,
            request_has_query_params,
            user_agent_header,
            accept_header_value,
            _globals,
            security,
            timeout_ms,
            get_serialized_body,
            url_override,
            http_headers,
        )

    def build_request(
        self,
        method,
        path,
        base_url,
        url_variables,
        request,
        request_body_required,
        request_has_path_params,
        request_has_query_params,
        user_agent_header,
        accept_header_value,
        _globals=None,
        security=None,
        timeout_ms: Optional[int] = None,
        get_serialized_body: Optional[
            Callable[[], Optional[SerializedRequestBody]]
        ] = None,
        url_override: Optional[str] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Request:
        client = self.sdk_configuration.client
        return self.build_request_with_client(
            client,
            method,
            path,
            base_url,
            url_variables,
            request,
            request_body_required,
            request_has_path_params,
            request_has_query_params,
            user_agent_header,
            accept_header_value,
            _globals,
            security,
            timeout_ms,
            get_serialized_body,
            url_override,
            http_headers,
        )

    def build_request_with_client(
        self,
        client,
        method,
        path,
        base_url,
        url_variables,
        request,
        request_body_required,
        request_has_path_params,
        request_has_query_params,
        user_agent_header,
        accept_header_value,
        _globals=None,
        security=None,
        timeout_ms: Optional[int] = None,
        get_serialized_body: Optional[
            Callable[[], Optional[SerializedRequestBody]]
        ] = None,
        url_override: Optional[str] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> httpx.Request:
        query_params = {}

        url = url_override
        if url is None:
            url = utils.generate_url(
                self.get_url(base_url, url_variables),
                path,
                request if request_has_path_params else None,
                _globals if request_has_path_params else None,
            )

            query_params = utils.get_query_params(
                request if request_has_query_params else None,
                _globals if request_has_query_params else None,
            )
        else:
            # Pick up the query parameter from the override so they can be
            # preserved when building the request later on (necessary as of
            # httpx 0.28).
            parsed_override = urlparse(str(url_override))
            query_params = parse_qs(parsed_override.query, keep_blank_values=True)

        headers = utils.get_headers(request, _globals)
        headers["Accept"] = accept_header_value
        headers[user_agent_header] = self.sdk_configuration.user_agent

        if security is not None:
            if callable(security):
                security = security()

        if security is not None:
            security_headers, security_query_params = utils.get_security(security)
            headers = {**headers, **security_headers}
            query_params = {**query_params, **security_query_params}

        serialized_request_body = SerializedRequestBody()
        if get_serialized_body is not None:
            rb = get_serialized_body()
            if request_body_required and rb is None:
                raise ValueError("request body is required")

            if rb is not None:
                serialized_request_body = rb

        if (
            serialized_request_body.media_type is not None
            and serialized_request_body.media_type
            not in (
                "multipart/form-data",
                "multipart/mixed",
            )
        ):
            headers["content-type"] = serialized_request_body.media_type

        if http_headers is not None:
            for header, value in http_headers.items():
                headers[header] = value

        timeout = timeout_ms / 1000 if timeout_ms is not None else None

        return client.build_request(
            method,
            url,
            params=query_params,
            content=serialized_request_body.content,
            data=serialized_request_body.data,
            files=serialized_request_body.files,
            headers=headers,
            timeout=timeout,
        )

    def do_request(
        self,
        hook_ctx,
        request,
        error_status_codes,
        stream=False,
        retry_config: Optional[Tuple[RetryConfig, List[str]]] = None,
    ) -> httpx.Response:
        client = self.sdk_configuration.client
        logger = self.sdk_configuration.debug_logger

        def do():
            http_res = None
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    BeforeRequestContext(hook_ctx), request
                )
                logger.debug(
                    "Request:\nMethod: %s\nURL: %s\nHeaders: %s\nBody: %s",
                    req.method,
                    req.url,
                    req.headers,
                    get_body_content(req),
                )
                http_res = client.send(req, stream=stream)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), None, e
                )
                if e is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise e

            if http_res is None:
                logger.debug("Raising no response SDK error")
                raise models.SDKError("No response received")

            logger.debug(
                "Response:\nStatus Code: %s\nURL: %s\nHeaders: %s\nBody: %s",
                http_res.status_code,
                http_res.url,
                http_res.headers,
                "<streaming response>" if stream else http_res.text,
            )

            if utils.match_status_codes(error_status_codes, http_res.status_code):
                result, err = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), http_res, None
                )
                if err is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise err
                if result is not None:
                    http_res = result
                else:
                    logger.debug("Raising unexpected SDK error")
                    raise models.SDKError("Unexpected error occurred")

            return http_res

        if retry_config is not None:
            http_res = utils.retry(do, utils.Retries(retry_config[0], retry_config[1]))
        else:
            http_res = do()

        if not utils.match_status_codes(error_status_codes, http_res.status_code):
            http_res = self.sdk_configuration.get_hooks().after_success(
                AfterSuccessContext(hook_ctx), http_res
            )

        return http_res

    async def do_request_async(
        self,
        hook_ctx,
        request,
        error_status_codes,
        stream=False,
        retry_config: Optional[Tuple[RetryConfig, List[str]]] = None,
    ) -> httpx.Response:
        client = self.sdk_configuration.async_client
        logger = self.sdk_configuration.debug_logger

        async def do():
            http_res = None
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    BeforeRequestContext(hook_ctx), request
                )
                logger.debug(
                    "Request:\nMethod: %s\nURL: %s\nHeaders: %s\nBody: %s",
                    req.method,
                    req.url,
                    req.headers,
                    get_body_content(req),
                )
                http_res = await client.send(req, stream=stream)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), None, e
                )
                if e is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise e

            if http_res is None:
                logger.debug("Raising no response SDK error")
                raise models.SDKError("No response received")

            logger.debug(
                "Response:\nStatus Code: %s\nURL: %s\nHeaders: %s\nBody: %s",
                http_res.status_code,
                http_res.url,
                http_res.headers,
                "<streaming response>" if stream else http_res.text,
            )

            if utils.match_status_codes(error_status_codes, http_res.status_code):
                result, err = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), http_res, None
                )
                if err is not None:
                    logger.debug("Request Exception", exc_info=True)
                    raise err
                if result is not None:
                    http_res = result
                else:
                    logger.debug("Raising unexpected SDK error")
                    raise models.SDKError("Unexpected error occurred")

            return http_res

        if retry_config is not None:
            http_res = await utils.retry_async(
                do, utils.Retries(retry_config[0], retry_config[1])
            )
        else:
            http_res = await do()

        if not utils.match_status_codes(error_status_codes, http_res.status_code):
            http_res = self.sdk_configuration.get_hooks().after_success(
                AfterSuccessContext(hook_ctx), http_res
            )

        return http_res
