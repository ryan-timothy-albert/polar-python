"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from jsonpath import JSONPath
from polar_sh import models, utils
from polar_sh._hooks import HookContext
from polar_sh.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Dict, Optional, Union, cast

class Products(BaseSDK):
    
    
    def list(
        self, *,
        security: Union[models.ProductsListSecurity, models.ProductsListSecurityTypedDict],
        request: Optional[Union[models.ProductsListRequest, models.ProductsListRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.ProductsListResponse:
        r"""List Products

        List products.

        :param security: 
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.ProductsListRequest)
        request = cast(models.ProductsListRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/products/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsListSecurity),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="products:list", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        def next_func() -> Optional[models.ProductsListResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            page = request.page if not request.page is None else 0
            next_page = page + 1
            
            num_pages = JSONPath("$.pagination.max_page").parse(body)
            if len(num_pages) == 0 or num_pages[0] <= page:
                return None

            if not http_res.text:
                return None
            results = JSONPath("$.items").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 0
            if len(results[0]) < limit:
                return None

            return self.list(
                request=models.ProductsListRequest(
                    organization_id=request.organization_id,
                    is_archived=request.is_archived,
                    is_recurring=request.is_recurring,
                    benefit_id=request.benefit_id,
                    type=request.type,
                    page=next_page,
                    limit=request.limit,
                ),
                retries=retries,
            )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.ProductsListResponse(result=utils.unmarshal_json(http_res.text, Optional[models.ListResourceProduct]), next=next_func)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def list_async(
        self, *,
        security: Union[models.ProductsListSecurity, models.ProductsListSecurityTypedDict],
        request: Optional[Union[models.ProductsListRequest, models.ProductsListRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.ProductsListResponse:
        r"""List Products

        List products.

        :param security: 
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.ProductsListRequest)
        request = cast(models.ProductsListRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/v1/products/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsListSecurity),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="products:list", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        def next_func() -> Optional[models.ProductsListResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            page = request.page if not request.page is None else 0
            next_page = page + 1
            
            num_pages = JSONPath("$.pagination.max_page").parse(body)
            if len(num_pages) == 0 or num_pages[0] <= page:
                return None

            if not http_res.text:
                return None
            results = JSONPath("$.items").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 0
            if len(results[0]) < limit:
                return None

            return self.list(
                request=models.ProductsListRequest(
                    organization_id=request.organization_id,
                    is_archived=request.is_archived,
                    is_recurring=request.is_recurring,
                    benefit_id=request.benefit_id,
                    type=request.type,
                    page=next_page,
                    limit=request.limit,
                ),
                retries=retries,
            )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return models.ProductsListResponse(result=utils.unmarshal_json(http_res.text, Optional[models.ListResourceProduct]), next=next_func)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def create(
        self, *,
        security: Union[models.ProductsCreateSecurity, models.ProductsCreateSecurityTypedDict],
        request: Union[models.ProductsCreateProductCreate, models.ProductsCreateProductCreateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Create Product

        Create a product.

        :param security: 
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.ProductsCreateProductCreate)
        request = cast(models.ProductsCreateProductCreate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/products/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsCreateSecurity),
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.ProductsCreateProductCreate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="products:create", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def create_async(
        self, *,
        security: Union[models.ProductsCreateSecurity, models.ProductsCreateSecurityTypedDict],
        request: Union[models.ProductsCreateProductCreate, models.ProductsCreateProductCreateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Create Product

        Create a product.

        :param security: 
        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, models.ProductsCreateProductCreate)
        request = cast(models.ProductsCreateProductCreate, request)
        
        req = self.build_request(
            method="POST",
            path="/v1/products/",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsCreateSecurity),
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.ProductsCreateProductCreate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="products:create", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def retrieve(
        self, *,
        security: Union[models.ProductsGetSecurity, models.ProductsGetSecurityTypedDict],
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Get Product

        Get a product by ID.

        :param security: 
        :param id: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.ProductsGetRequest(
            id=id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/products/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsGetSecurity),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="products:get", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def retrieve_async(
        self, *,
        security: Union[models.ProductsGetSecurity, models.ProductsGetSecurityTypedDict],
        id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Get Product

        Get a product by ID.

        :param security: 
        :param id: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.ProductsGetRequest(
            id=id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/products/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsGetSecurity),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="products:get", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def update(
        self, *,
        security: Union[models.ProductsUpdateSecurity, models.ProductsUpdateSecurityTypedDict],
        id: str,
        product_update: Union[models.ProductUpdate, models.ProductUpdateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Update Product

        Update a product.

        :param security: 
        :param id: 
        :param product_update: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.ProductsUpdateRequest(
            id=id,
            product_update=utils.get_pydantic_model(product_update, models.ProductUpdate),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/v1/products/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsUpdateSecurity),
            get_serialized_body=lambda: utils.serialize_request_body(request.product_update, False, False, "json", models.ProductUpdate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="products:update", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def update_async(
        self, *,
        security: Union[models.ProductsUpdateSecurity, models.ProductsUpdateSecurityTypedDict],
        id: str,
        product_update: Union[models.ProductUpdate, models.ProductUpdateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Update Product

        Update a product.

        :param security: 
        :param id: 
        :param product_update: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.ProductsUpdateRequest(
            id=id,
            product_update=utils.get_pydantic_model(product_update, models.ProductUpdate),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/v1/products/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsUpdateSecurity),
            get_serialized_body=lambda: utils.serialize_request_body(request.product_update, False, False, "json", models.ProductUpdate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="products:update", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def update_benefits(
        self, *,
        security: Union[models.ProductsUpdateBenefitsSecurity, models.ProductsUpdateBenefitsSecurityTypedDict],
        id: str,
        product_benefits_update: Union[models.ProductBenefitsUpdate, models.ProductBenefitsUpdateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Update Product Benefits

        Update benefits granted by a product.

        :param security: 
        :param id: 
        :param product_benefits_update: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.ProductsUpdateBenefitsRequest(
            id=id,
            product_benefits_update=utils.get_pydantic_model(product_benefits_update, models.ProductBenefitsUpdate),
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/products/{id}/benefits",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsUpdateBenefitsSecurity),
            get_serialized_body=lambda: utils.serialize_request_body(request.product_benefits_update, False, False, "json", models.ProductBenefitsUpdate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="products:update_benefits", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def update_benefits_async(
        self, *,
        security: Union[models.ProductsUpdateBenefitsSecurity, models.ProductsUpdateBenefitsSecurityTypedDict],
        id: str,
        product_benefits_update: Union[models.ProductBenefitsUpdate, models.ProductBenefitsUpdateTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ProductOutput]:
        r"""Update Product Benefits

        Update benefits granted by a product.

        :param security: 
        :param id: 
        :param product_benefits_update: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.ProductsUpdateBenefitsRequest(
            id=id,
            product_benefits_update=utils.get_pydantic_model(product_benefits_update, models.ProductBenefitsUpdate),
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/products/{id}/benefits",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(security, models.ProductsUpdateBenefitsSecurity),
            get_serialized_body=lambda: utils.serialize_request_body(request.product_benefits_update, False, False, "json", models.ProductBenefitsUpdate),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="products:update_benefits", oauth2_scopes=[], security_source=security),
            request=req,
            error_status_codes=["403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProductOutput])
        if utils.match_response(http_res, "403", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.NotPermittedData)
            raise models.NotPermitted(data=data)
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ResourceNotFoundData)
            raise models.ResourceNotFound(data=data)
        if utils.match_response(http_res, "422", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.HTTPValidationErrorData)
            raise models.HTTPValidationError(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
